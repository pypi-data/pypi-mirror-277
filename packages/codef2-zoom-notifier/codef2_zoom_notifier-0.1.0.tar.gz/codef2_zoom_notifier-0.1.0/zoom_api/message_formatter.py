import logging
from .config import MESSAGE_SUBJECT, MESSAGE_DIVIDER, AI_GENERATED_MESSAGE

def format_for_zoom_message(message_body):
    logging.info("Formatting data to send as Zoom messages")   
    message = ""
    message += MESSAGE_SUBJECT
    message += MESSAGE_DIVIDER + '\n'
    message += message_body + '\n\n'
    message += MESSAGE_DIVIDER
    message += AI_GENERATED_MESSAGE
    return message
