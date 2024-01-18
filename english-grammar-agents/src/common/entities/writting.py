"""
This script contains classes that  define the different options for Writting.
classes:
    WrittingFixType(Enum) -> define the writte properly and writte only grammar cases.
"""
# Standard imports
from enum import Enum

# Internal imports
from modules.prompts import same_grammar_fix, writte_properly


class WrittingFixType(Enum):
    """
    This Enum class defines all possible writting types.
    All options are mapped directly to the corresponding module
    """
    WRITE_PROPERLY = writte_properly
    WRITE_SAME_GRAMMAR_FIXED = same_grammar_fix
