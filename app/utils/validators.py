"""
Validator utilities for inputs.
"""


def validate_destination(value: str) -> str:
    """Ensure destination is one of fb, ig or both."""
    allowed = {"fb", "ig", "both"}
    if value not in allowed:
        raise ValueError(f"Destination must be one of {allowed}")
    return value
