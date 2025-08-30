"""
Backoff utilities for retrying operations.
"""

import time
from typing import Callable, Any


def retry_with_backoff(func: Callable[..., Any], retries: int = 3, base_delay: float = 1.0):
    """Simple exponential backoff decorator."""

    def wrapper(*args, **kwargs):
        attempt = 0
        while True:
            try:
                return func(*args, **kwargs)
            except Exception:
                attempt += 1
                if attempt > retries:
                    raise
                delay = base_delay * (2 ** (attempt - 1))
                time.sleep(delay)

    return wrapper
