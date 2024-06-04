from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _get_security_groups(self, AUTH_TOKEN, URL, DEBUG):
    API_URL = f"{URL}/api/lookup/22?lookupKey=99e8767a-00ba-4758-b9c2-e07b52c47016"

    # Create header for the request
    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    if (DEBUG):
        print(f"API_URL: {API_URL}\nMETHOD: GET")

    retries = 0
    while True:
        try:
            # Send the request
            RESPONSE = requests.get(API_URL, headers= HEADERS)
            
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
                _api_exception_handler(RESPONSE, "Get Security Groups failed")

        except:
            _api_exception_handler(RESPONSE, f"Get Security Groups failed")
            
    return RESPONSE.json()