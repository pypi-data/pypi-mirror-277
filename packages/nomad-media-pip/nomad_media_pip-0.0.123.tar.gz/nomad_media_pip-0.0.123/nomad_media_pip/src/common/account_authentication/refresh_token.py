from nomad_media_pip.src.helpers.send_request import _send_request

def _refresh_token(AUTH_TOKEN, URL, REFRESH_TOKEN, DEBUG):
    API_URL = f"{URL}/api/account/refresh-token"

    BODY = {
        "refreshToken": REFRESH_TOKEN
    }

    return _send_request(None, AUTH_TOKEN, "Refresh Token", API_URL, "POST", None, BODY, DEBUG)    