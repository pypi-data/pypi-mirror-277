from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _move_schedule_item(self, AUTH_TOKEN, URL, ID, ITEM_ID, PREVIOUS_ITEM, DEBUG):
    
    API_URL = f"{URL}/api/admin/schedule/{ID}/item/{ITEM_ID}/move"

    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    BODY = {
        "previous_item": PREVIOUS_ITEM
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST")

    retries = 0
    while True:
        try:
            RESPONSE = requests.post(API_URL, headers= HEADERS, data=json.dumps(BODY))

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
                _api_exception_handler(RESPONSE, "Move Schedule Item Failed")

        except:
            _api_exception_handler(RESPONSE, "Move Schedule Item Failed")
            
    return RESPONSE.json()