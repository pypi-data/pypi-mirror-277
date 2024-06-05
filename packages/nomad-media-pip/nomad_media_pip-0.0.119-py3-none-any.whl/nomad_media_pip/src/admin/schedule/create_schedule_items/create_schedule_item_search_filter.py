from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _create_schedule_item_search_filter(self, AUTH_TOKEN, URL, SCHEDULE_ID, COLLECTIONS, DAYS,
                                        DURATION_TIME_CODE, END_SEARCH_DATE, 
                                        END_SEARCH_DURATION_IN_MINUTES, END_TIME_CODE,
                                        PREVIOUS_ITEM, RELATED_CONTENT, SEARCH_DATE,
                                        SEARCH_DURATION_IN_MINUTES, SEARCH_FILTER_TYPE,
                                        TAGS, TIME_CODE, DEBUG):
    
    API_URL = f"{URL}/api/admin/schedule/{SCHEDULE_ID}/item"
    
    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    BODY = {
        "collections": COLLECTIONS,
        "days": DAYS,
        "durationTimeCode": DURATION_TIME_CODE,
        "endSearchDate": END_SEARCH_DATE,
        "endSearchDurationInMinutes": END_SEARCH_DURATION_IN_MINUTES,
        "endTimeCode": END_TIME_CODE,
        "previousItem": PREVIOUS_ITEM,
        "relatedContent": RELATED_CONTENT,
        "scheduleItemType": "1",
        "searchDate": SEARCH_DATE,
        "searchDurationInMinutes": SEARCH_DURATION_IN_MINUTES,
        "searchFilterType": SEARCH_FILTER_TYPE,
        "sourceType": "2",
        "tags": TAGS,
        "timeCode": TIME_CODE
    }
    
    if DEBUG:
        print(f"URL: {API_URL},\nMETHOD: POST,\nBODY: {json.dumps(BODY, indent=4)}")
    
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
                _api_exception_handler(RESPONSE, "Create Schedule Item Search Filter Failed")

        except:
            _api_exception_handler(RESPONSE, "Create Schedule Item Search Filter Failed")
            
    return RESPONSE.json()