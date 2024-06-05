from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests

def _delete_annotation(self, AUTH_TOKEN, URL, ASSET_ID, ANNOTATION_ID, DEBUG):

    API_URL = f"{URL}/api/asset/{ASSET_ID}/annotation/{ANNOTATION_ID}"

    HEADERS = {
        "Content-Type": "application/json",
      	"Authorization": "Bearer " + AUTH_TOKEN
    }

    if DEBUG:
        print(f"URL: {API_URL}\nMETHOD: DELETE")

    try:
        RESPONSE = requests.delete(API_URL, headers=HEADERS)

        if not RESPONSE.ok:
            raise Exception()
        
        return RESPONSE.json()
    
    except:
        _api_exception_handler(RESPONSE, "Delete annotation failed")