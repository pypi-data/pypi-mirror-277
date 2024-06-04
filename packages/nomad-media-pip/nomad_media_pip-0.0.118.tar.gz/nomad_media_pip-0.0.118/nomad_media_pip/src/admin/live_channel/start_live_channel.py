from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.admin.live_channel.live_channel_statuses import _LIVE_CHANNEL_STATUSES
from nomad_media_pip.src.admin.live_channel.wait_for_live_channel_status import _wait_for_live_channel_status

import json, requests, time

MAX_RETRIES = 2

def _start_live_channel(self, AUTH_TOKEN, URL, CHANNEL_ID, WAIT_FOR_START, DEBUG):
    API_URL = f"{URL}/api/liveChannel/{CHANNEL_ID}/start"

    # Create header for the request
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    if (DEBUG):
        print(f"API_URL: {API_URL}\nMETHOD: POST")

    retries = 0
    while True:
        try:
            # Send the request
            RESPONSE = requests.post(API_URL, headers= HEADERS)

            if RESPONSE.ok:
                if WAIT_FOR_START == False: return
                # Wait for the Live Channel to be running
                _wait_for_live_channel_status(self, AUTH_TOKEN, URL, CHANNEL_ID, _LIVE_CHANNEL_STATUSES["Running"], 1200, 20, DEBUG)

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
                _api_exception_handler(RESPONSE, f"Start Live Channel {CHANNEL_ID} failed")
                
        except:
            _api_exception_handler(RESPONSE, f"Start Live Channel {CHANNEL_ID} failed")

