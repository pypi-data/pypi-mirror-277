from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, time
MAX_RETRIES = 2

def _archive_asset(self, AUTH_TOKEN, URL, ASSET_ID, DEBUG):

    API_URL = f"{URL}/api/admin/asset/{ASSET_ID}/archive"

    HEADERS = {
        "Content-Type": "application/json",
      	"Authorization": "Bearer " + AUTH_TOKEN
    }

    if DEBUG:
        print(f"URL: {API_URL}\nMETHOD: POST")

    retries = 0
    while True:
        try:
            RESPONSE = requests.post(API_URL, headers=HEADERS)

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
                _api_exception_handler(RESPONSE, "Archive asset failed")

        except:
            _api_exception_handler(RESPONSE, "Archive asset failed")
            
    return RESPONSE.json()