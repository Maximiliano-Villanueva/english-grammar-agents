"""
This script contains classes that represent different prompt messages available in the prompts folder.
classes:
    - PromptTemplate(Enum) -> Define the different kind of prompts for human and system.
"""
# Standard imports
from enum import Enum


class PromptTemplate(Enum):
    """
    This Enum class represents the different types of messages inside the scripts in modules.prompts.
    The value of these attributes are then used to load the corresponding templates from the prompt modules.
    """
    SYSTEM_MESSAGE = "SYSTEM_MESSAGE"
    HUMAN_MESSAGE = "HUMAN_MESSAGE"