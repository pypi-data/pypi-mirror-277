from nomad_media_pip.src.helpers.send_request import _send_request

def _upload_asset_part(FILE, URL, PART, DEBUG):
    if not FILE or not URL or not PART:
        raise Exception("Upload Part: Invalid API call")
    
    OPEN_FILE = open(FILE, "rb")
    OPEN_FILE.seek(PART["startingPosition"])
    BODY = OPEN_FILE.read(PART["endingPosition"] + 1 - PART["startingPosition"])
    OPEN_FILE.close()

    return _send_request(URL, "Upload Asset Part", PART["uploadUrl"], "PUT", BODY, False, DEBUG)
