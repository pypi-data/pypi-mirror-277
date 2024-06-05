from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _deactivate_content_user_track(self, AUTH_TOKEN, URL, SESSION_ID, CONTENT_ID,
                                CONTENT_DEFINITION_ID, DEACTIVATE, DEBUG):

    API_URL = f"{URL}/api/content/{CONTENT_DEFINITION_ID}/user-track/{CONTENT_ID}/{SESSION_ID}/{DEACTIVATE}"

    # Create header for the request
    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: DELETE")

    retries = 0
    while True:
        try:
            # Send the request
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
                _api_exception_handler(RESPONSE, "Deactivate content user track failed")

        except:
            _api_exception_handler(RESPONSE, "Deactivate content user track failed")
            
    return RESPONSE.json()