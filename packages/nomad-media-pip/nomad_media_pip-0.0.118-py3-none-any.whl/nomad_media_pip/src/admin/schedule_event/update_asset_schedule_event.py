from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.admin.schedule_event.event_types import _EVENT_TYPES
from nomad_media_pip.src.admin.schedule_event.get_asset_schedule_event import _get_asset_schedule_event

import requests, json, time
MAX_RETRIES = 2

def _update_asset_schedule_event(self, AUTH_TOKEN, URL, ID, CHANNEL_ID, ASSET, IS_LOOP, 
                                 DURATION_TIME_CODE, DEBUG):
        
    API_URL = f"{URL}/api/liveChannel/{CHANNEL_ID}/liveScheduleEvent"

    SCHEDULE_EVENT_INFO = _get_asset_schedule_event(self, AUTH_TOKEN, URL, CHANNEL_ID, 
                                                    ID, DEBUG)
    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    BODY = {
        "type": {
            "id": _EVENT_TYPES["videoAsset"],
            "description": "Video Asset"
        }
    }

    BODY['id'] = ID if ID and ID != SCHEDULE_EVENT_INFO['id'] else SCHEDULE_EVENT_INFO['id']
    BODY['isLoop'] = IS_LOOP if IS_LOOP and IS_LOOP != SCHEDULE_EVENT_INFO['isLoop'] else SCHEDULE_EVENT_INFO['isLoop']
    BODY['channelId'] = CHANNEL_ID if CHANNEL_ID and CHANNEL_ID != SCHEDULE_EVENT_INFO['channelId'] else SCHEDULE_EVENT_INFO['channelId']
    BODY['durationTimeCode'] = DURATION_TIME_CODE if DURATION_TIME_CODE and DURATION_TIME_CODE != SCHEDULE_EVENT_INFO['durationTimeCode'] else SCHEDULE_EVENT_INFO['durationTimeCode']
    BODY['asset'] = ASSET if ASSET and ASSET != SCHEDULE_EVENT_INFO['asset'] else SCHEDULE_EVENT_INFO['asset']
    
    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: PUT,\nBODY: {json.dumps(BODY, indent=4)}")
    
    retries = 0
    while True:
        try:
            RESPONSE = requests.put(API_URL, headers= HEADERS, data= json.dumps(BODY))
            
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
                _api_exception_handler(RESPONSE, "Update Asset Schedule Event Failed")

        except:
            _api_exception_handler(RESPONSE, "Update Asset Schedule Event Failed")
        
    return RESPONSE.json()