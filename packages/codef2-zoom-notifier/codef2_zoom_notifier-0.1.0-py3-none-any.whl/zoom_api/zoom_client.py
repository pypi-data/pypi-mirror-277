import logging
import math
import time
import requests
import base64
from .config import ZOOM_API_URL, TO_CONTACTS, ENV_LEVEL, ACCESS_TOKEN_URL, CLIENT_ID, CLIENT_SECRET, ACCOUNT_ID
from .message_formatter import format_for_zoom_message

def get_access_token():
    encoded_credentials = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()

    data = {
        "grant_type": "account_credentials",
        "account_id": ACCOUNT_ID
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}"
    }

    logging.info('Trying to obtain access token from Zoom')
    response = requests.post(ACCESS_TOKEN_URL, headers=headers, data=data)

    if response.status_code == 200:
        logging.info("Successfully obtained an access token from Zoom.")
        return response.json()["access_token"]
    else:
        logging.error("Failed to obtain access token.")
        logging.error(response.text)
        return None

def send_message_to_zoom_group(message, msg_category, msg_type):
    heading_color = "FF0000" if msg_type == 'Failure' else '008B21'
    access_token = get_access_token()
    if not access_token:
        return

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    if len(message) <= 25000:
        logging.info('Message within length limit no chunk needed')
        for contact in TO_CONTACTS:
            payload = {
                f"{'to_contact' if ENV_LEVEL == 'development' else 'to_channel' }": contact,
                "message": message,
                "at_items": [{"at_type": 2, "end_position": 0, "start_position": 0}],
                "rich_text": [
                    {"start_position": 0, "end_position": len(message)+1, "format_type": "Bold", "format_attr": ""},
                ]
            }
            try:
                response = requests.post(ZOOM_API_URL, headers=headers, json=payload)
                if response.status_code == 201:
                    logging.info(f"{msg_category} {msg_type} Message sent successfully to Zoom group {contact}!")
                    time.sleep(1)
                else:
                    logging.error(f"Failed to send {msg_category} {msg_type} message to Zoom group {contact}. Status Code: {response.status_code}")
                    logging.error(response.text)
            except Exception as e:
                logging.error(f"Failed to send {msg_category} {msg_type} message to Zoom group {contact}. Error: {e}")
        return
    
    chunk_size = 25000
    num_chunks = math.ceil(len(message) / chunk_size)

    for i in range(num_chunks):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size
        chunk_message = message[start_index:end_index]

        for contact in TO_CONTACTS:
            payload = {
                f"{'to_contact' if ENV_LEVEL == 'development' else 'to_channel' }": contact,
                "message": chunk_message,
                "at_items": [{"at_type": 2, "end_position": 0, "start_position": 0}],
                "rich_text": [
                    {"start_position": 0, "end_position": len(chunk_message) + 1, "format_type": "Bold", "format_attr": ""},
                ]
            }
            try:
                response = requests.post(ZOOM_API_URL, headers=headers, json=payload)
                if response.status_code == 201:
                    logging.info(f"{msg_category} {msg_type} Chunk {i+1}/{num_chunks} sent successfully to Zoom group {contact}!")
                    time.sleep(1)
                else:
                    logging.error(f"Failed to send {msg_category} {msg_type} Chunk {i+1}/{num_chunks} message to Zoom group {contact}. Status Code: {response.status_code}")
                    logging.error(response.text)
            except Exception as e:
                logging.error(f"Failed to send {msg_category} {msg_type} Chunk {i+1}/{num_chunks} message to Zoom group {contact}. Error: {e}")

def send_zoom_notification(message_body, message_category='unknown', message_type='failure'):
    if not message_body:
        logging.error('You Should Provide A Message Body')
        return
    try:
        logging.info("Preparing message for sending to Zoom group.")
        final_message = format_for_zoom_message(message_body)
        send_message_to_zoom_group(final_message, msg_category=message_category, msg_type=message_type.capitalize())
    except KeyError as ke:
        logging.error("Failed to send message to Zoom due to a KeyError.", exc_info=ke)
    except Exception as e:
        logging.error("Failed to send message to Zoom due to an unexpected error.", exc_info=e)
