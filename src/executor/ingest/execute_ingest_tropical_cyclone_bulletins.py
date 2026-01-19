"""
Execute ingest workflow for tropical cyclone bulletins data from the PAGASA-DOST website.

This module orchestrates the ingest helpers in `ingest_tropical_cyclone_bulletins` to ingest
artifacts and store them as a JSON files under `data/raw/tropical_cyclone_bulletins/` subdirectory
for further processing.

Main function:
- `ingest_tropical_cyclone_bulletins` - Runs the end-to-end ingest workflow
"""
from ingest.ingest_tropical_cyclone_bulletins import create_subdir

def ingest_tropical_cyclone_bulletins(
) -> None:
    """
    Executes the function in the
    `src.ingest_tropical_cyclone_bulletins.py`
    module to ingest the data from the tropical cyclone
    bulletins page of PAGASA-DOST website.
    """
    create_subdir()