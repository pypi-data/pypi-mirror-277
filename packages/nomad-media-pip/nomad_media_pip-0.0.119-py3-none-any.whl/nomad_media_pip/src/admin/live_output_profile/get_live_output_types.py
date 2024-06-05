from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _get_live_output_types(self, AUTH_TOKEN, URL, DEBUG):
    API_URL = f"{URL}/api/lookup/117"

    # Create header for the request
    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: GET")

    # Make the request
    retries = 0
    while True:
        try:
            RESPONSE = requests.get(API_URL, headers=HEADERS)
            
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
                _api_exception_handler(RESPONSE, "Get Output Types Failed")

        except:
            _api_exception_handler(RESPONSE, "Get Output Types Failed")
            
            
    return RESPONSE.json()["items"]