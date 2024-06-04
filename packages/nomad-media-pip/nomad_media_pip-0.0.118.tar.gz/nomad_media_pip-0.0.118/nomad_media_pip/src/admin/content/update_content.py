from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.admin.content.get_content import _get_content

import json, requests, time
from deepdiff import DeepDiff

MAX_RETRIES = 2

def _update_content(self, AUTH_TOKEN, URL, ID, CONTENT_DEFINITION_ID, PROPERTIES, 
                    LANGUAGE_ID, DEBUG):
    API_URL = f"{URL}/api/content/{ID}"
    
    HEADERS = {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + AUTH_TOKEN
    }

    try:
        BODY = _get_content(self, AUTH_TOKEN, URL, ID, CONTENT_DEFINITION_ID, None, DEBUG)

        if (BODY["contentDefinitionId"] != CONTENT_DEFINITION_ID): BODY["contentDefinitionId"] = CONTENT_DEFINITION_ID
        if (BODY.get("languageId") != LANGUAGE_ID): BODY["languageId"] = LANGUAGE_ID
        if (BODY["contentId"] != ID): BODY["contentId"] = ID

        _update_properties(BODY, PROPERTIES)

    except:
        BODY = {
            "contentDefinitionId": CONTENT_DEFINITION_ID,
            "contentId": ID,
            "languageId": LANGUAGE_ID,
            "properties": PROPERTIES
        }

    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST,\nBODY: {json.dumps(BODY, indent=4)}")

    retries = 0
    while True:
        try:
            RESPONSE = requests.put(API_URL, headers=HEADERS, data=json.dumps(BODY))

            if RESPONSE.ok:
                break

        except requests.exceptions.Timeout:
            if retries < MAX_RETRIES:
                retries += 1
                time.sleep(20)
            else:
                _api_exception_handler(RESPONSE, "Update Content failed")

        except:
            _api_exception_handler(RESPONSE, "Update Content failed")

    return RESPONSE.json()

def _update_properties(body, properties):
    for property, value in properties.items():
        if isinstance(value, list):
            for i in range(len(value)):
                if DeepDiff(body['properties'][property][i], value[i]):
                    body['properties'][property][i] = value[i]
        elif isinstance(value, dict):
            if DeepDiff(body['properties'][property], value):
                body['properties'][property] = value
        elif body['properties'].get(property) != value:
            body['properties'][property] = value

