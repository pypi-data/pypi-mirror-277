from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _get_audit(self, AUTH_TOKEN, URL, ID, DEBUG):
    API_URL = f"{URL}/api/admin/audit/{ID}"

    # Create header for the request
    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: GET")

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
                _api_exception_handler(RESPONSE, "Get audit failed")

        except:
            _api_exception_handler(RESPONSE, "Get audit failed")
            
    return RESPONSE.json()