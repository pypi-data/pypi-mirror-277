"""
This module provides functions to facilitate identifying and classifying
pregnancies from diagnostic and PROCEDURE codes.

OUTCOMES exports the full CODE list
OUTCOME_LIST exports a list of the outcome classifications
map_version_split exports 4 dataframes of outcome codes based on the CODE code_type
process_outcomes is the process to pass data in order to identify and classify pregnancy OUTCOMES
"""

from .outcome_map import OUTCOMES, OUTCOME_LIST
from .attach_map import map_version_split
from .process_outcome import process_outcomes
