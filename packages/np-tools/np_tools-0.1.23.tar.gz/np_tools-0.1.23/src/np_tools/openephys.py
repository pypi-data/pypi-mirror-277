"""Tools for working with Open Ephys raw data files."""
from __future__ import annotations

import doctest
import json
import pathlib
import tempfile
from typing import Any, Generator, Optional, Sequence, Iterable

import np_config
import np_logging

import np_tools.file_io as file_io


logger = np_logging.get_logger(__name__)

DEFAULT_PROBES = 'ABCDEF'


def is_new_ephys_folder(path: pathlib.Path) -> bool:
    """Look for any hallmarks of a v0.6.x Open Ephys recording in path or subfolders."""

    globs = (
        'Record Node*',
        'structure*.oebin',
    )
    components = tuple(_.replace('*', '') for _ in globs)

    if any(_.lower() in path.as_posix().lower() for _ in components):
        return True

    for glob in globs:
        if next(path.rglob(glob), None):
            return True
    return False

def correct_structure_oebin_files(dest: pathlib.Path) -> None:
    """
    Overwrites oebin files with correct metadata, removing entries for missing
    folders.
    
    - in cases of probes not being inserted, raw data may be removed or not copied
      over, and the structure.oebin will contain data paths for entries that don't exist
    - this function will remove those entries from the structure.oebin file
    """
    logger.debug('Checking structure.oebin for missing folders...')
    recording_dirs = dest.rglob('recording[0-9]*')
    for recording_dir in recording_dirs:
        if not recording_dir.is_dir():
            continue
        oebin_path = recording_dir / 'structure.oebin'
        if not (oebin_path.is_symlink() or oebin_path.exists()):
            logger.warning(f'No structure.oebin found in {recording_dir}')
            continue
        logger.debug(f'Examining oebin: {oebin_path} for correction')
        if oebin_path.is_symlink():
            oebin_path = np_config.normalize_path(oebin_path.readlink())
        oebin_obj = read_oebin(oebin_path)
        any_removed = False
        for subdir_name in ('events', 'continuous'):    
            subdir = oebin_path.parent / subdir_name
            # iterate over copy of list so as to not disrupt iteration when elements are removed
            for device in [device for device in oebin_obj[subdir_name]]:
                if not (subdir / device['folder_name']).exists():
                    logger.info(f'{device["folder_name"]} not found in {subdir}, removing from structure.oebin')
                    oebin_obj[subdir_name].remove(device)
                    any_removed = True
        if any_removed:
            oebin_path.unlink()
            oebin_path.write_text(json.dumps(oebin_obj, indent=4))
            logger.debug('Overwrote structure.oebin with corrected strcuture.oebin')
            
def is_complete_ephys_folder(path: pathlib.Path) -> bool:
    """Look for all hallmarks of a complete v0.6.x Open Ephys recording."""
    # TODO use structure.oebin to check for completeness
    if not is_new_ephys_folder(path):
        return False
    for glob in ('continuous.dat', 'spike_times.npy', 'spike_clusters.npy'):
        if not next(path.rglob(glob), None):
            logger.debug(f'Could not find {glob} in {path}')
            return False
    return True


def is_valid_ephys_folder(
    path: pathlib.Path, min_size_gb: Optional[int | float] = None,
) -> bool:
    """Check a single dir of raw data for size and v0.6.x+ Open Ephys."""
    if not path.is_dir():
        return False
    if not is_new_ephys_folder(path):
        return False
    if min_size_gb is not None and file_io.dir_size(path) < min_size_gb * 1024**3: # GB
        return False
    return True


def get_ephys_root(path: pathlib.Path) -> pathlib.Path:
    """Returns the parent of the first `Record Node *` found in the supplied
    path.

    >>> get_ephys_root(pathlib.Path('A:/test/Record Node 0/Record Node test')).as_posix()
    'A:/test'
    """
    if 'Record Node' not in path.as_posix():
        raise ValueError(
            f"Could not find 'Record Node' in {path} - is this a valid raw ephys path?"
        )
    return next(
        p.parent
        for p in path.parents
        if 'Record Node'.lower() in p.name.lower()
    )



def get_filtered_ephys_paths_relative_to_record_node_parents(
    toplevel_ephys_path: pathlib.Path,
    specific_recording_dir_names: Iterable[str] | None = None
    ) -> Generator[tuple[pathlib.Path, pathlib.Path], None, None]:
    """For restructuring the raw ephys data in a session folder, we want to
    discard superfluous recording folders and only keep the "good" data, but
    with the overall directory structure relative to `Record Node*` folders intact.
    
    Supply a top-level path that contains `Record Node *`
    subfolders somewhere in its tree. 
    
    Returns a generator akin to `path.rglob('Record Node*')` except:
    - only paths associated with the "good" ephys data are returned (with some
    assumptions made about the ephys session)
    - a tuple of two paths is supplied:
        - `(abs_path, abs_path.relative_to(record_node.parent))`
        ie. path[1] should always start with `Record Node *`
    
    Expectation is:
    - `/npexp_path/ephys_*/Record Node */ recording1 / ... / continuous.dat`
    
    ie. 
    - one recording per `Record Node *` folder
    - one subfolder in `npexp_path/` per `Record Node *` folder (following the
    pipeline `*_probeABC` / `*_probeDEF` convention for recordings split across two
    drives)
    

    Many folders have:
    - `/npexp_path/Record Node */ recording*/ ...` 
    
    ie.
    - multiple recording folders per `Record Node *` folder
    - typically there's one proper `recording` folder: the rest are short,
    aborted recordings during setup
    
    We filter out the superfluous small recording folders here.
    
    Some folders (Templeton) have:
    - `/npexp_path/Record Node */ ...`
    
    ie.
    - contents of expected ephys subfolders directly deposited in npexp_path
    
    >>> path = pathlib.Path("//allen/programs/mindscope/workgroups/dynamicrouting/PilotEphys/Task 2 pilot/DRpilot_686176_20231206/DRpilot_686176_20231206")
    >>> len(tuple(get_filtered_ephys_paths_relative_to_record_node_parents(path)))
    230
    >>> len(tuple(get_filtered_ephys_paths_relative_to_record_node_parents(path, 'recording1')))
    230
    >>> len(tuple(get_filtered_ephys_paths_relative_to_record_node_parents(path, 'recording2')))
    230
    >>> len(tuple(get_filtered_ephys_paths_relative_to_record_node_parents(path, ('recording1', 'recording2'))))
    456
    """
    def is_recording_name(name: str) -> bool:
        return name.startswith('recording') and name[9:].isdigit()
    
    if specific_recording_dir_names:
        if isinstance(specific_recording_dir_names, str):
            specific_recording_dir_names = (specific_recording_dir_names,)
        for name in specific_recording_dir_names:
            if not is_recording_name(name):
                raise ValueError(f'specific_recording_dir_names must be in the format "recording1": got {name!r}')

    record_nodes = toplevel_ephys_path.rglob('Record Node*')
    
    if specific_recording_dir_names:
        for record_node in record_nodes:
            for abs_path in record_node.rglob('*'):          
                is_recording_child = any(is_recording_name(name) for name in abs_path.parts)
                is_matching_name = any(name in abs_path.parts for name in specific_recording_dir_names)
                if is_recording_child and not is_matching_name:
                    continue
                yield abs_path, abs_path.relative_to(record_node.parent) 
    else: 
        for record_node in record_nodes:
            superfluous_recording_dirs = tuple(
                _.parent for _ in get_superfluous_oebin_paths(record_node)
            )
            logger.debug(f'Found {len(superfluous_recording_dirs)} superfluous recording dirs to exclude: {superfluous_recording_dirs}')
            
            for abs_path in record_node.rglob('*'):
                is_superfluous_path = abs_path in superfluous_recording_dirs or any(_ in abs_path.parents for _ in superfluous_recording_dirs)
                
                if is_superfluous_path:
                    continue
                
                yield abs_path, abs_path.relative_to(record_node.parent)
        
       
def get_raw_ephys_subfolders(
    path: pathlib.Path, min_size_gb: Optional[int | float] = None
) -> tuple[pathlib.Path, ...]:
    """
    Return raw ephys recording folders, defined as the root that Open Ephys
    records to, e.g. `A:/1233245678_366122_20220618_probeABC`.
    """ 

    subfolders = set()

    for f in pathlib.Path(path).rglob('continuous.dat'):

        if any(
            k in f.as_posix().lower()
            for k in [
                'sorted',
                'extracted',
                'curated',
            ]
        ):
            # skip sorted/extracted folders
            continue

        subfolders.add(get_ephys_root(f))

    if min_size_gb is not None:
        subfolders = {_ for _ in subfolders if file_io.dir_size(_) < min_size_gb * 1024**3}

    return tuple(sorted(list(subfolders), key=lambda s: str(s)))


# - If we have probeABC and probeDEF raw data folders, each one has an oebin file:
#     we'll need to merge the oebin files and the data folders to create a single session
#     that can be processed in parallel
def get_single_oebin_path(path: pathlib.Path) -> pathlib.Path:
    """Get the path to a single structure.oebin file in a folder of raw ephys data.

    - There's one structure.oebin per `recording*` folder
    - Raw data folders may contain multiple `recording*` folders
    - Datajoint expects only one structure.oebin file per Session for sorting
    - If we have multiple `recording*` folders, we assume that there's one
        good folder - the largest - plus some small dummy / accidental recordings
    """
    if not path.is_dir():
        raise ValueError(f'{path} is not a directory')

    oebin_paths = tuple(path.rglob('structure*.oebin'))
        
    if not oebin_paths:
        raise FileNotFoundError(f'No structure.oebin file found in {path}')

    if len(oebin_paths) == 1:
        return oebin_paths[0]
    
    oebin_parents = (_.parent for _ in oebin_paths)
    dir_sizes = tuple(file_io.dir_size(_) for _ in oebin_parents)
    return oebin_paths[dir_sizes.index(max(dir_sizes))]


def get_superfluous_oebin_paths(path: pathlib.Path) -> tuple[pathlib.Path, ...]:
    """Get the paths to any oebin files in `recording*` folders that are not
    the largest in a folder of raw ephys data. 
    
    Companion to `get_single_oebin_path`.
    """
    
    all_oebin_paths = tuple(path.rglob('structure*.oebin'))
    
    if len(all_oebin_paths) == 1:
        return tuple()
    
    return tuple(set(all_oebin_paths) - {(get_single_oebin_path(path))})


def assert_xml_files_match(paths: Sequence[pathlib.Path]) -> None:
    """Check that all xml files are identical, as they should be for
    recordings split across multiple locations e.g. A:/*_probeABC, B:/*_probeDEF
    or raise an error.
    
    Update: xml files on two nodes can be created at slightly different times, so their `date`
    fields may differ. Everything else should be identical.
    """
    if not all(s == '.xml' for s in [p.suffix for p in paths]):
        raise ValueError('Not all paths are XML files')
    if not all(p.is_file() for p in paths):
        raise FileNotFoundError(
            'Not all paths are files, or they do not exist'
        )
    if not file_io.checksums_match(paths):
        
        # if the files are the same size and were created within +/- 1 second
        # of each other, we'll assume they're the same
        
        created_times = tuple(p.stat().st_ctime for p in paths)
        created_times_equal = all(created_times[0] - 1 <= t <= created_times[0] + 1 for t in created_times[1:])
        
        sizes = tuple(p.stat().st_size for p in paths)
        sizes_equal = all(s == sizes[0] for s in sizes[1:])
        
        if not (sizes_equal and created_times_equal):
            raise AssertionError('XML files do not match')


def get_merged_oebin_file(
    paths: Sequence[pathlib.Path], exclude_probe_names: Optional[Sequence[str]] = None
) -> pathlib.Path:
    """Merge two or more structure.oebin files into one.

    For recordings split across multiple locations e.g. A:/*_probeABC,
    B:/*_probeDEF
    - if items in the oebin files have 'folder_name' values that match any
    entries in `exclude_probe_names`, they will be removed from the merged oebin
    """
    if isinstance(paths, pathlib.Path):
        return paths
    if any(not p.suffix == '.oebin' for p in paths):
        raise ValueError('Not all paths are .oebin files')
    if len(paths) == 1:
        return paths[0]

    # ensure oebin files can be merged - if from the same exp they will have the same settings.xml file
    assert_xml_files_match(
        [p / 'settings.xml' for p in [o.parent.parent.parent for o in paths]]
    )

    logger.debug(f'Creating merged oebin file from {paths}')
    merged_oebin = dict()
    for oebin_path in sorted(paths):
        oebin_data = read_oebin(oebin_path)

        for key in oebin_data:

            # skip if already in merged oebin
            if merged_oebin.get(key) == oebin_data[key]:
                continue

            # 'continuous', 'events', 'spikes' are lists, which we want to concatenate across files
            if isinstance(oebin_data[key], list):
                for item in oebin_data[key]:
                    
                    # skip if already in merged oebin
                    if item in merged_oebin.get(key, []):
                        continue
                    
                    # skip probes in excl list (ie. not inserted)
                    if exclude_probe_names and any(
                        p.lower() in item.get('folder_name', '').lower()
                        for p in exclude_probe_names
                    ):
                        continue
                    
                    # insert in merged oebin
                    merged_oebin.setdefault(key, []).append(item)

    if not merged_oebin:
        raise ValueError('No data found in structure.oebin files')
    
    merged_oebin_path = pathlib.Path(tempfile.gettempdir()) / 'structure.oebin'
    merged_oebin_path.write_text(json.dumps(merged_oebin, indent=4))
    return merged_oebin_path


def read_oebin(path: str | pathlib.Path) -> dict[str, Any]:
    return json.loads(pathlib.Path(path).read_bytes())


if __name__ == '__main__':
    doctest.testmod()
