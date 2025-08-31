import pytest
from datetime import datetime
from app.services.content_engine import ContentEngine


def test_schedule_post_not_implemented():
    engine = ContentEngine()
    with pytest.raises(NotImplementedError):
        engine.schedule_post(text="Hello", publish_time=datetime.utcnow(), destination="fb")
