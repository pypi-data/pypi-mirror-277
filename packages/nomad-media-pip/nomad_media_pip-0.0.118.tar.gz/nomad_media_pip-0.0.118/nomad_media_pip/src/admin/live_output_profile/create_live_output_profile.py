from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _create_live_output_profile(self, AUTH_TOKEN, URL, NAME, OUTPUT_TYPE, ENABLED, AUDIO_BITRATE,
                        OUTPUT_STREAM_KEY, OUTPUT_URL, SECONDARY_OUTPUT_STREAM_KEY,
                        SECONDARY_OUTPUT_URL, VIDEO_BITRATE, VIDEO_BITRATE_MODE,
                        VIDEO_CODEC, VIDEO_FRAMES_PER_SECOND, VIDEO_HEIGHT, VIDEO_WIDTH,
                        DEBUG):

    API_URL = f"{URL}/api/liveOutputProfile"

    HEADERS = {
        'Content-Type': 'application/json',
        "Authorization": "Bearer " + AUTH_TOKEN
    }

    BODY = {
        "name": NAME,
        "outputType": OUTPUT_TYPE,
        "enabled": ENABLED,
        "audioBitrate": AUDIO_BITRATE,
        "outputStreamKey": OUTPUT_STREAM_KEY,
        "outputUrl": OUTPUT_URL,
        "secondaryOutputStreamKey": SECONDARY_OUTPUT_STREAM_KEY,
        "secondaryOutputUrl": SECONDARY_OUTPUT_URL,
        "videoBitrate": VIDEO_BITRATE,
        "videoBitrateMode": VIDEO_BITRATE_MODE,
        "videoCodec": VIDEO_CODEC,
        "videoFramesPerSecond": VIDEO_FRAMES_PER_SECOND,
        "videoHeight": VIDEO_HEIGHT,
        "videoWidth": VIDEO_WIDTH
    }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST,\nBODY: {json.dumps(BODY, indent=4)}")

    retries = 0
    while True:
        try:
            RESPONSE = requests.post(API_URL, headers=HEADERS, data=json.dumps(BODY))

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
                _api_exception_handler(RESPONSE, "Create Live Output Proflie Failed")

        except:
            _api_exception_handler(RESPONSE, "Create Live Output Proflie Failed")
            
    return RESPONSE.json()