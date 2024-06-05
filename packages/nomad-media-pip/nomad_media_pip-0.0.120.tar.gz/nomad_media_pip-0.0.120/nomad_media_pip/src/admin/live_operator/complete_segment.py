from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _complete_segment(self, AUTH_TOKEN, URL, ID, RELATED_CONTENT_IDS, TAG_IDS, DEBUG):
    API_URL = f"{URL}/api/admin/liveOperator/{ID}/completeSegment"

    HEADERS = {
        "Authorization": "Bearer " +  AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    BODY = {
        "liveOperatorId": ID,
    }

    if RELATED_CONTENT_IDS and isinstance(RELATED_CONTENT_IDS, list) and len(RELATED_CONTENT_IDS) > 0:
        BODY["relatedContent"] = [{"id": id} for id in RELATED_CONTENT_IDS]
    
    if TAG_IDS and isinstance(TAG_IDS, list) and len(TAG_IDS) > 0:
        BODY["tags"] = [{"id": id} for id in RELATED_CONTENT_IDS]

    if (DEBUG):
        print(f"API_URL: {API_URL}\nMETHOD: POST\nBODY: {json.dumps(BODY, indent= 4)}")

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
                _api_exception_handler(RESPONSE, f"Completing segment for Live Channel {ID} failed")

        except:
            _api_exception_handler(RESPONSE, f"Completing segment for Live Channel {ID} failed")