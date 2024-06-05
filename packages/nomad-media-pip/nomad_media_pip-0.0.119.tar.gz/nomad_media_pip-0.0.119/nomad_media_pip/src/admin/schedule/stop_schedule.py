from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _stop_schedule(self, AUTH_TOKEN, URL, ID, FORCE_STOP, DEBUG):
    if FORCE_STOP == None:
        FORCE_STOP = False

    API_URL = f"{URL}/api/admin/schedule/{ID}/stop?force={FORCE_STOP}"

    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST")

    retries = 0
    while True:
        try:
            RESPONSE = requests.post(API_URL, headers= HEADERS)

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
                _api_exception_handler(RESPONSE, "Stop Schedule Failed")

        except:
            _api_exception_handler(RESPONSE, "Stop Schedule Failed")


    return RESPONSE.json()