from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _get_config(self, AUTH_TOKEN, URL, CONFIG_TYPE, DEBUG):
    API_URL = f"{URL}/api/config?configType={CONFIG_TYPE}"

    HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + AUTH_TOKEN
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: GET")

    retries = 0
    while True:
        try:
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
                _api_exception_handler(RESPONSE, "Get Config Failed")

        except:
            _api_exception_handler(RESPONSE, "Get Config Failed")
            
    return RESPONSE.json()