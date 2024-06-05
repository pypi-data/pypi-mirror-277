from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _create_schedule_item_playlist_schedule(self, AUTH_TOKEN, URL, SCHEUDLE_ID, DAYS, 
                                            DURATION_TIME_CODE, END_TIME_CODE, 
                                            PLAYLIST_SCHEDULE, PREVIOUS_ITEM, TIME_CODE, 
                                            DEBUG):
        
    API_URL = f"{URL}/api/admin/schedule/{SCHEUDLE_ID}/item"
    
    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }
    
    BODY = {
        "days": DAYS,
        "durationTimeCode": DURATION_TIME_CODE,
        "endTimeCode": END_TIME_CODE,
        "playlistSchedule": PLAYLIST_SCHEDULE,
        "previousItem": PREVIOUS_ITEM,
        "scheduleItemType": "2",
        "sourceType": "1",
        "timeCode": TIME_CODE
    }
    
    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST,\nBODY: {json.dumps(BODY, indent=4)}")
    
    retries = 0
    while True:
        try:
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
                _api_exception_handler(RESPONSE, "Create Schedule Item Playlist Schedule Failed")

        except:
            _api_exception_handler(RESPONSE, "Create Schedule Item Playlist Schedule Failed")
            
    return RESPONSE.json()