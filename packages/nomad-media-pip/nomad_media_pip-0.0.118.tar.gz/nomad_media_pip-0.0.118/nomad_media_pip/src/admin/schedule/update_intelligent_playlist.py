from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.admin.schedule.get_intelligent_playlist import _get_intelligent_playlist
from nomad_media_pip.src.admin.schedule.get_schedule_items import _get_schedule_items

import requests, json, time

MAX_RETRIES = 2

def _update_intelligent_playlist(self, AUTH_TOKEN, URL, ID, COLLECTIONS, END_SEARCH_DATE, 
                                 END_SEARCH_DURATION_IN_MINUTES, NAME, RELATED_CONTENT, 
                                 SEARCH_DATE, SEARCH_DURATION_IN_MINUTES, SEARCH_FILTER_TYPE, 
                                 TAGS, THUMBNAIL_ASSET, DEBUG):

    SCHEDULE_API_URL = f"{URL}/api/admin/schedule/{ID}"

    PLAYLIST_INFO = _get_intelligent_playlist(self, AUTH_TOKEN, URL, ID, DEBUG)

    HEADERS = {
        "Authorization": "Bearer " + AUTH_TOKEN,
        "Content-Type": "application/json"
    }

    SCHEDULE_BODY = {
        "name": NAME or PLAYLIST_INFO.get("name"),
        "scheduleType": "4",
        "thumbnailAsset": THUMBNAIL_ASSET or PLAYLIST_INFO.get("thumbnailAsset"),
        "scheduleStatus": PLAYLIST_INFO.get("scheduleStatus"),
        "status": PLAYLIST_INFO.get("status")
    }

    if DEBUG:
        print(f"URL: {SCHEDULE_API_URL},\nMETHOD: PUT,\nBODY: {json.dumps(SCHEDULE_BODY)}")

    retries = 0
    while True:
        try:
            SCHEDULE_RESPONSE = requests.put(SCHEDULE_API_URL, headers= HEADERS, data=json.dumps(SCHEDULE_BODY))

            if SCHEDULE_RESPONSE.ok:
                break

            if SCHEDULE_RESPONSE.status_code == 403:
                self.refresh_token()
            else:
                raise Exception()
            
        except requests.exceptions.Timeout:
            if retries < MAX_RETRIES:
                retries += 1
                time.sleep(20)
            else:
                _api_exception_handler(SCHEDULE_RESPONSE, "Update Intelligent Playlist Failed")

        except:
            _api_exception_handler(SCHEDULE_RESPONSE, "Update Intelligent Playlist Failed")
            
    SCHEDULE_INFO = SCHEDULE_RESPONSE.json()

    ITEM_INFO = _get_schedule_items(self, AUTH_TOKEN, URL, ID, DEBUG)
    ITEM = ITEM_INFO[0]

    ITEM_API_URL = f"{SCHEDULE_API_URL}/item/{ITEM['id']}"

    ITEM_BODY = {
        'id': ITEM['id'],
        'collections': COLLECTIONS if COLLECTIONS != [] else ITEM.get("collections"),
        'endSearchDate': END_SEARCH_DATE if END_SEARCH_DATE else ITEM.get("endSearchDate"),
        'endSearchDurationInMinutes': END_SEARCH_DURATION_IN_MINUTES if END_SEARCH_DURATION_IN_MINUTES else ITEM.get("endSearchDurationInMinutes"),
        'relatedContent': RELATED_CONTENT if RELATED_CONTENT != [] else ITEM.get("relatedContent"),
        'scheduleItemType': "2",
        'searchDate': SEARCH_DATE if SEARCH_DATE else ITEM.get("searchDate"),
        'searchDurationInMinutes': SEARCH_DURATION_IN_MINUTES if SEARCH_DURATION_IN_MINUTES else ITEM.get("searchDurationInMinutes"),
        'searchFilterType': SEARCH_FILTER_TYPE if SEARCH_FILTER_TYPE else ITEM.get("searchFilterType"),
        'sourceType': "2",
        'tags': TAGS if TAGS != [] else ITEM.get("tags")
    }

    if DEBUG:
        print(f"URL: {ITEM_API_URL},\nMETHOD: PUT,\nBODY: {json.dumps(ITEM_BODY)}")

    retries = 0
    while True:
        try:
            RESPONSE = requests.put(ITEM_API_URL, headers= HEADERS, data=json.dumps(ITEM_BODY))
            
            if RESPONSE.ok:
                ITEM_INFO = RESPONSE.json()

                for param in SCHEDULE_INFO:
                    ITEM_INFO[param] = SCHEDULE_INFO[param]

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
                _api_exception_handler(RESPONSE, "Update Intelligent Playlist Failed")
                
        except:
            _api_exception_handler(RESPONSE, "Update Intelligent Playlist Failed")

    return ITEM_INFO