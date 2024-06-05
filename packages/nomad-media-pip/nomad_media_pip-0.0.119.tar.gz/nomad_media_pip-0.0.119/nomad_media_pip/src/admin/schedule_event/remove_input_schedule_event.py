from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _remove_input_schedule_event(self, AUTH_TOKEN, URL, CHANNEL_ID, INPUT_ID, DEBUG):
    API_URL = f"{URL}/api/liveChannel/{CHANNEL_ID}/liveScheduleEvent/{INPUT_ID}" 

    # Create header for the request
    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    if DEBUG:
        print(f"API URL: {API_URL}\nMETHOD: DELETE")

    retries = 0
    while True:
        try:
            RESPONSE = requests.delete(API_URL, headers= HEADERS)

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
                _api_exception_handler(RESPONSE, "Remove Input Schedule Event failed")

        except:
            _api_exception_handler(RESPONSE, "Remove Input Schedule Event failed")