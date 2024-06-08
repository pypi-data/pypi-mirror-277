import json
import requests
import uuid
from datetime import datetime


class Tracker:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def track_page_view(self, page_name):
        self._capture_event('page_view', {'page_name': page_name})

    def track_button_click(self, button_name):
        self._capture_event('button_click', {'button_name': button_name})

    def _capture_event(self, event_name, event_data):
        device_id = str(uuid.uuid4())
        session_id = str(uuid.uuid4())
        event = {
            'event_name': event_name,
            'event_data': event_data,
            'device_id': device_id,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
        }
        print('Event captured:', event)

        # Perform the network request
        try:
            response = requests.post(self.endpoint, json=event)
            response.raise_for_status()
        except Exception as e:
            print('Error capturing event:', e)

