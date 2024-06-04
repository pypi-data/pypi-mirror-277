from nomad_media_pip.src.admin.schedule_event.event_types import _EVENT_TYPES
from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import json, requests, time
MAX_RETRIES = 2

def _add_input_schedule_event(self, AUTH_TOKEN, URL, CHANNEL_ID, INPUT, BACKUP_INPUT, 
                              ON_AIR_TIME, PREVIOUS_ID, DEBUG):
    API_URL = f"{URL}/api/liveChannel/" + CHANNEL_ID + "/liveScheduleEvent"

    # Create header for the request
    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    # Build the payload BODY
    BODY = {
        "channelId": CHANNEL_ID,
        "fixedOnAirTimeUtc": ON_AIR_TIME,
        "type": {
            "id": _EVENT_TYPES["liveInput"],
            "description": "Live Input"
        },
        "liveInput": INPUT,
        "previousId": PREVIOUS_ID
    }

    if BACKUP_INPUT:
        BODY["liveInput2"] = BACKUP_INPUT

    if DEBUG:
        print(f"API URL: {API_URL}\nMETHOD: POST\nBODY: {json.dumps(BODY, indent=4)}")

    retries = 0
    while True:
        try:
            # Send the request
            RESPONSE = requests.post(API_URL,  headers= HEADERS, data= json.dumps(BODY))
        
            if RESPONSE.ok:
                break
            
            if RESPONSE.status_code == 403:
                self.refresh_token()
            else:
                raise Exception()

        except requests.exceptions.Timeout:
            if retries < MAX_RETRIES:
                retries += 1
                time.sleep(20)
            else:
                _api_exception_handler(RESPONSE, "Add Input Schedule Event failed")

        except:
            _api_exception_handler(RESPONSE, "Add Input Schedule Event failed")

    return RESPONSE.json()