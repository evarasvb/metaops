"""
Scheduled tasks for MetaOps.
"""


def catalog_sync_job():
    """Synchronize catalog every 2 hours."""
    # TODO: call catalog sync service
    raise NotImplementedError("Catalog sync job not implemented")


def post_dispatcher_job():
    """Publish scheduled posts."""
    # TODO: dispatch due posts to Meta
    raise NotImplementedError("Post dispatch job not implemented")


def daily_report_job():
    """Send daily report at 09:00 America/Santiago."""
    # TODO: compile and send daily report
    raise NotImplementedError("Daily report job not implemented")
