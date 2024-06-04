from nomad_media_pip.src.admin.schedule_event.event_types import _EVENT_TYPES
from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import json, requests, time
MAX_RETRIES = 2

def _add_asset_schedule_event(self, AUTH_TOKEN, URL, CHANNEL_ID, ASSET, IS_LOOP,
                              DURATION_TIME_CODE, PREVIOUS_ID, DEBUG):
    API_URL = f"{URL}/api/liveChannel/{CHANNEL_ID}/liveScheduleEvent" 

    # Create header for the request
    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    # Build the payload BODY
    BODY = {
        "isLoop": IS_LOOP,
        "channelId": CHANNEL_ID,
        "durationTimeCode": DURATION_TIME_CODE,
        "previousId": PREVIOUS_ID,
        "type": {
            "id": _EVENT_TYPES["videoAsset"],
            "description": "Video-Asset"
        },
        "asset": ASSET,
    }

    if DEBUG:
        print(f"API URL: {API_URL}\nMETHOD: POST\nBODY: {json.dumps(BODY, indent=4)}")

    retries = 0
    while True:
        try:
            # Send the request
            RESPONSE = requests.post(API_URL, headers= HEADERS, data= json.dumps(BODY))
            
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
                _api_exception_handler(RESPONSE, "Add Asset Schedule Event failed")

        except:
            _api_exception_handler(RESPONSE, "Add Asset Schedule Event failed")

    return RESPONSE.json()