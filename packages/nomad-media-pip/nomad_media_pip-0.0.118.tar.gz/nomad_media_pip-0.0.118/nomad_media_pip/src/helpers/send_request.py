from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import json, requests, time
MAX_RETRIES = 2
SLEEP_TIME = 20

def _send_request(self, AUTH_TOKEN, FUNCTION_NAME, URL, METHOD_TYPE, BODY, IS_AUTH, DEBUG):
    
    HEADERS = {
        "Content-Type": "application/json"
    }

    if IS_AUTH: HEADERS["Authorization"] = f"Bearer {AUTH_TOKEN}"

    if DEBUG: print(f"URL: {URL}\nMETHOD: {METHOD_TYPE}\n" + f"BODY: {json.dumps(BODY, indent=4) }" if BODY else "")

    retries = 0
    while True:
        try:
            RESPONSE = requests.request(METHOD_TYPE, URL, headers = HEADERS, data = json.dumps(BODY) if BODY else None)

            if RESPONSE.ok:
                break

            if RESPONSE.status_code == 403:
                self.refresh_token()
            else:
                raise Exception()
            
        except requests.exceptions.Timeout:
            if retries < MAX_RETRIES:
                retries += 1
                time.sleep(SLEEP_TIME)
            else:
                _api_exception_handler(RESPONSE, f"{METHOD_TYPE} request failed")
        
        except Exception as e:
            _api_exception_handler(RESPONSE, f"{FUNCTION_NAME} failed: {e}")

    return RESPONSE.json()