"""
This script contains classes that represent the strategies defined in the project.
classes:
    - Strategy (Enum) -> Define the strategies available for writting
    - StrategySummarize(Enum) -> Define the strategies available for summarizing
"""
# Standard imports
from enum import Enum


class Strategy(Enum):
    """
    This Enum class represents the different strategies to follow when prompting.
    The value of these attributes are then used to load the corresponding templates from the prompt modules.
    """
    ZERO_SHOT = "ZERO_SHOT"
    FEW_SHOT = "FEW_SHOT"
    CHAIN_OF_THOUGHT = "CHAIN_OF_THOUGHT"


class StrategySummarize(Enum):
    """
    This Enum class represents the different strategies to follow when summarizing.
    """
    STUFF = "STUFF"
    MAP_REDUCE = "MAP_REDUCE"