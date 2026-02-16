"""
Input Validation and Sanitization Utilities.

Provides functions to validate and clean user inputs
before processing to prevent issues and improve security.
"""
import re
from typing import Tuple, Optional


# Constants for validation
MAX_INPUT_LENGTH = 10000  # Maximum characters per message
MIN_INPUT_LENGTH = 1      # Minimum characters per message
MAX_MESSAGES_HISTORY = 50 # Maximum messages to keep in history


def validate_user_input(
    text: str,
    max_length: int = MAX_INPUT_LENGTH,
    min_length: int = MIN_INPUT_LENGTH
) -> Tuple[bool, str, Optional[str]]:
    """
    Validate user input for chat messages.
    
    Args:
        text: The user input to validate
        max_length: Maximum allowed characters
        min_length: Minimum required characters
        
    Returns:
        Tuple of (is_valid, cleaned_text, error_message)
        - is_valid: Whether the input is valid
        - cleaned_text: The sanitized input (if valid)
        - error_message: Description of validation failure (if invalid)
    """
    # Check for None or empty
    if text is None:
        return False, "", "Input cannot be empty"
    
    # Strip whitespace
    cleaned = text.strip()
    
    # Check minimum length
    if len(cleaned) < min_length:
        return False, "", f"Input must be at least {min_length} character(s)"
    
    # Check maximum length
    if len(cleaned) > max_length:
        return False, "", f"Input exceeds maximum length of {max_length} characters"
    
    # Sanitize the input
    sanitized = sanitize_input(cleaned)
    
    return True, sanitized, None


def sanitize_input(text: str) -> str:
    """
    Sanitize user input by removing potentially problematic content.
    
    This is a basic sanitization - Azure OpenAI has its own content filtering.
    
    Args:
        text: The text to sanitize
        
    Returns:
        Sanitized text
    """
    # Remove null bytes
    text = text.replace('\x00', '')
    
    # Normalize whitespace (but preserve legitimate line breaks)
    text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces/tabs to single space
    text = re.sub(r'\n{3,}', '\n\n', text)  # More than 2 newlines to 2
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def truncate_messages(
    messages: list,
    max_messages: int = MAX_MESSAGES_HISTORY
) -> list:
    """
    Truncate message history to prevent context overflow.
    
    Keeps the most recent messages while ensuring we don't
    exceed token limits for the API.
    
    Args:
        messages: List of message dictionaries
        max_messages: Maximum number of messages to keep
        
    Returns:
        Truncated list of messages
    """
    if len(messages) <= max_messages:
        return messages
    
    # Keep the most recent messages
    return messages[-max_messages:]


def estimate_tokens(text: str) -> int:
    """
    Rough estimate of token count for a string.
    
    This is a simple heuristic - actual token count varies by model.
    Rule of thumb: ~4 characters per token for English text.
    
    Args:
        text: The text to estimate tokens for
        
    Returns:
        Estimated token count
    """
    return len(text) // 4


def validate_session_id(session_id: str) -> bool:
    """
    Validate that a session ID is properly formatted.
    
    Args:
        session_id: The session ID to validate
        
    Returns:
        True if valid UUID format
    """
    uuid_pattern = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        re.IGNORECASE
    )
    return bool(uuid_pattern.match(session_id))
