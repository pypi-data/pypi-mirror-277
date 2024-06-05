from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.helpers.slugify import _slugify
from nomad_media_pip.src.admin.live_channel.live_channel_statuses import _LIVE_CHANNEL_STATUSES
from nomad_media_pip.src.admin.live_channel.get_security_groups import _get_security_groups
from nomad_media_pip.src.admin.live_channel.wait_for_live_channel_status import _wait_for_live_channel_status
from nomad_media_pip.src.admin.live_channel.live_channel_types import _LIVE_CHANNEL_TYPES

import json, requests, time

MAX_RETRIES = 2

def _create_live_channel(self, AUTH_TOKEN, URL, NAME, THUMBNAIL_IMAGE, ARCHIVE_FOLDER_ASSET, 
                        ENABLE_HIGH_AVAILABILITY, ENABLE_LIVE_CLIPPING, IS_SECURE_OUTPUT, 
                        OUTPUT_SCREENSHOTS, TYPE, EXTERNAL_URL, SECURITY_GROUPS, DEBUG):
    
    API_URL = f"{URL}/api/liveChannel"

    # Create header for the request
    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    # Build the payload BODY
    BODY = {
        "name": NAME,
        "routeName": _slugify(NAME),
        "enableHighAvailability": ENABLE_HIGH_AVAILABILITY,
        "enableLiveClipping": ENABLE_LIVE_CLIPPING,
        "isSecureOutput": IS_SECURE_OUTPUT,
        "outputScreenshots": OUTPUT_SCREENSHOTS,
        "type": { "id": _LIVE_CHANNEL_TYPES[TYPE] }
    }

    if THUMBNAIL_IMAGE:
        BODY["thumbnailImage"] = { "id": THUMBNAIL_IMAGE }

    if ARCHIVE_FOLDER_ASSET:
        BODY["archiveFolderAsset"] = { "id": ARCHIVE_FOLDER_ASSET }

    # Set the appropriate fields based on the channel type
    if (TYPE == _LIVE_CHANNEL_TYPES["External"]):
        BODY["externalUrl"] = EXTERNAL_URL

    if SECURITY_GROUPS:
        NOMAD_SECURITY_GROUPS = _get_security_groups(self, AUTH_TOKEN, URL, DEBUG)

        BODY['securityGroups'] = [
        {
            'description': group['description'],
            'id': group['id']
        }
        for group in NOMAD_SECURITY_GROUPS
        if group['description'] in SECURITY_GROUPS
    ]

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST\nBODY: {json.dumps(BODY, indent=4)}")

    retries = 0
    while True:
        try:
            # Send the request
            RESPONSE = requests.post(API_URL, headers= HEADERS, data= json.dumps(BODY))
            INFO = json.loads(RESPONSE.text)

            if RESPONSE.ok:    
                _wait_for_live_channel_status(self, AUTH_TOKEN, URL, INFO["id"], _LIVE_CHANNEL_STATUSES["Idle"], 120, 2, DEBUG)
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
                _api_exception_handler(RESPONSE, f"Created Live Channel {NAME} failed")

        except:
            _api_exception_handler(RESPONSE, f"Created Live Channel {NAME} failed")

    return RESPONSE.json()