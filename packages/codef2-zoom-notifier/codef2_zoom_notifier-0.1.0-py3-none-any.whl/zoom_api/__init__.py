from .zoom_client import send_zoom_notification
from .logging_config import configure_logging

configure_logging()

__all__ = ['send_zoom_notification']
