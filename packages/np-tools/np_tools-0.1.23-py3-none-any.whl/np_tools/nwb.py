from __future__ import annotations

import pathlib
import tempfile
from typing import Optional
import uuid

import np_logging
import pynwb

logger = np_logging.getLogger(__name__)


def init_nwb(
    session: np_session.Session,
    description: str = 'Data and metadata for a Neuropixels ecephys session',
) -> pynwb.NWBFile:
    """
    Init `NWBFile` with minimum required arguments from an
    `np_session.Session` instance.
    """
    return pynwb.NWBFile(
        session_description=description,
        identifier=str(uuid.uuid4()),  # globally unique for this nwb - not human-readable
        session_start_time=session.start,
    )
    

def load_nwb(
    nwb_path: str | pathlib.Path,
    ) -> pynwb.NWBFile:
    """Load `pynb.NWBFile` instance from path."""
    logger.info(f'Loading .nwb file at {nwb_path}')
    with pynwb.NWBHDF5IO(nwb_path, mode='r') as f:
        return f.read()


def save_nwb(
    nwb_file: pynwb.NWBFile,
    output_path: Optional[str | pathlib.Path] = None,
    ) -> pathlib.Path:
    """
    Write `pynb.NWBFile` instance to disk.
    
    Temp dir is used if `output_path` isn't provided.
    """
    if output_path is None:
        output_path = pathlib.Path(tempfile.mkdtemp()) / f'{nwb_file.session_id}.nwb'
    
    nwb_file.set_modified()
    # not clear if this is necessary, but suggested by docs:
    # https://pynwb.readthedocs.io/en/stable/_modules/pynwb.html

    logger.info(f'Writing .nwb file `{nwb_file.session_id!r}` to {output_path}')
    with pynwb.NWBHDF5IO(output_path, mode='w') as f:
        f.write(nwb_file, cache_spec=True)
    logger.debug(f'Writing complete for nwb file `{nwb_file.session_id!r}`')
    return output_path
