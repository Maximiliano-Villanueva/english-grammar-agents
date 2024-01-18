# Standard imports
import re
import unicodedata


def dictionary_check(message: str):
    """
    This function is meant to check each word in a dictionary.
    This could help reduce efforts from the llm and making sure which words are incorrect from the beggining
    """


def remove_special_chars(message: str) -> str:
    """
    Remove special characters from an input string.

    This function uses a regular expression to replace all non-alphanumeric
    characters (excluding spaces) in the input string with an empty string.

    Parameters:
    message (str): The input string from which special characters are to be removed.

    Returns:
    str: The input string without special characters.
    """
    # Regular expression to match any character that is not a letter, digit or space
    pattern = r'[^a-zA-Z0-9\s]'
    return re.sub(pattern, '', message)


def normalize_unicode(message: str) -> str:
    """
    Normalize Unicode characters in a string to a consistent form.

    This function converts the input string to 'Normalization Form C' (NFC),
    where the characters are composed to a single character. This helps in
    maintaining a consistent representation of Unicode characters.

    Parameters:
    message (str): The input string containing Unicode characters.

    Returns:
    str: A normalized string with Unicode characters in NFC form.
    """
    if not isinstance(message, str):
        raise ValueError("Input must be a string")

    normalized_string = unicodedata.normalize('NFC', message)
    return normalized_string


def sanitize_input_prompt_injection(message: str) -> str:
    """
    Sanitize a string to prevent prompt injection attacks.

    This function removes or escapes characters and patterns that could be used
    maliciously to alter the intended behavior of a system processing the string.

    Parameters:
    message (str): The input string to be sanitized.

    Returns:
    str: A sanitized version of the input string.
    """
    if not isinstance(message, str):
        raise ValueError("Input must be a string")

    # Basic sanitization strategy: Escaping special characters
    sanitized_string = re.sub(r'([\'\"\\])', r'\\\1', message)

    return sanitized_string