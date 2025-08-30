"""
Scheduler setup using APScheduler.
"""

from apscheduler.schedulers.background import BackgroundScheduler


def get_scheduler() -> BackgroundScheduler:
    """Create and configure an APScheduler instance."""
    scheduler = BackgroundScheduler(timezone="America/Santiago")
    return scheduler
