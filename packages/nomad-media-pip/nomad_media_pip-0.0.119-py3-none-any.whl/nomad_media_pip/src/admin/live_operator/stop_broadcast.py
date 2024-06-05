from nomad_media_pip.src.admin.live_operator.wait_for_live_operator_status import _wait_for_live_operator_status
from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _stop_broadcast(self, AUTH_TOKEN, URL, ID, DEBUG):
    API_URL = f"{URL}/api/admin/liveOperator/{ID}/stop"

    HEADERS = {
        "Authorization": "Bearer " +  AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    if (DEBUG):
        print(f"API_URL: {API_URL}\nMETHOD: POST")

    retries = 0
    while True:
        try:
            RESPONSE = requests.post(API_URL, headers= HEADERS)

            if RESPONSE.ok:
                _wait_for_live_operator_status(self, AUTH_TOKEN, URL, ID, "Idle", 1200, 20, DEBUG)
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
                _api_exception_handler(RESPONSE, f"Stopping broadcast for Live Channel {ID} failed")

        except:
            _api_exception_handler(RESPONSE, f"Stopping broadcast for Live Channel {ID} failed")