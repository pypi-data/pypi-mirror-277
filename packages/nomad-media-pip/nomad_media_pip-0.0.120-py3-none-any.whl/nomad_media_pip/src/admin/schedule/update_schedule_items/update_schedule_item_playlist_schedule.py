from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.admin.schedule.get_schedule_item import _get_schedule_item

import requests, json, time
MAX_RETRIES = 2

def _update_schedule_item_playlist_schedule(self, AUTH_TOKEN, URL, ID, ITEM_ID, DAYS,
                                            DURATION_TIME_CODE, END_TIME_CODE, 
                                            PLAYLIST_SCHEDULE, TIME_CODE, DEBUG):
    
    SCHEDULE_ITEM = _get_schedule_item(self, AUTH_TOKEN, URL, ID, ITEM_ID, DEBUG)

    API_URL = f"{URL}/api/admin/schedule/{ID}/item/{ITEM_ID}"

    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    BODY = {
        "days": DAYS or SCHEDULE_ITEM.get("days"),
        "durationTimeCode": DURATION_TIME_CODE or SCHEDULE_ITEM.get("durationTimeCode"),
        "endTimeCode": END_TIME_CODE or SCHEDULE_ITEM.get("endTimeCode"),
        "playlistSchedule": PLAYLIST_SCHEDULE or SCHEDULE_ITEM.get("playlistSchedule"),
        "scheduleItemType": "2",
        "sourceType": "1",
        "timeCode": TIME_CODE or SCHEDULE_ITEM.get("timeCode")
    }

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
                _api_exception_handler(RESPONSE, "Update Schedule Item Playlist Schedule Failed")

        except:
            _api_exception_handler(RESPONSE, "Update Schedule Item Playlist Schedule Failed")
            
    return RESPONSE.json()