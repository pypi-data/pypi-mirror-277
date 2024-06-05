from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _delete_user_content_security_data(self, AUTH_TOKEN, URL, CONTENT_ID, CONTENT_DEFINITION_ID, USER_ID, EMAIL, ID, KEY_NAME, EXPIRATON_DATE, DEBUG):
    
    API_URL = f"{URL}/api/admin/user/userContentSecurity/delete"
    
    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    BODY = {
        "contentId": CONTENT_ID,
        "contentDefinitionId": CONTENT_DEFINITION_ID,
        "userId": USER_ID,
        "email": EMAIL,
        "id": ID,
        "keyName": KEY_NAME,
        "expirationDate": EXPIRATON_DATE
    }
    
    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST\nBODY: {json.dumps(BODY, indent=4)}")
    
    retries = 0
    while True:
        try:
            RESPONSE = requests.post(API_URL, headers= HEADERS, data= json.dumps(BODY))
            
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
                _api_exception_handler(RESPONSE, "Delete User Content Security Data Failed")

        except:
            _api_exception_handler(RESPONSE, "Delete User Content Security Data Failed")