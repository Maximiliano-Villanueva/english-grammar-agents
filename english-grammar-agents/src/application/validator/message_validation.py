"""
This script contains implementation to validate messages from the user
"""
# Internal imports
from common.entities.api.message import Message


def validate_input_message(message: Message) -> bool:
    """
    Validate input message.
    
    Return bool: True if message is not empty
    """
    return len(message.data) > 0