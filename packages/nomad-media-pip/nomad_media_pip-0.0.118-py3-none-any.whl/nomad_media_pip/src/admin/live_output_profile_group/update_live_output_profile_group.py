from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler
from nomad_media_pip.src.admin.live_output_profile_group.get_live_output_profile_group import _get_live_output_profile_group

import requests, json, time
MAX_RETRIES = 2

def _update_live_output_profile_group(self, AUTH_TOKEN, URL, LIVE_OUTPUT_PROFILE_GROUP_ID, NAME, IS_ENABLED, MANIFEST_TYPE, IS_DEFAULT_GROUP, LIVE_OUTPUT_TYPE, ARCHIVE_LIVE_OUTPUT_PROFILE, LIVE_OUTPUT_PROFILES, DEBUG):

	API_URL = f"{URL}/api/liveOutputProfileGroup"

	HEADERS = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {AUTH_TOKEN}"
	}

	PROFILE_GROUP_INFO = _get_live_output_profile_group(self, AUTH_TOKEN, URL, LIVE_OUTPUT_PROFILE_GROUP_ID, DEBUG)

	BODY = {
		"id": LIVE_OUTPUT_PROFILE_GROUP_ID or PROFILE_GROUP_INFO.get("id"),
		"name": NAME or PROFILE_GROUP_INFO.get("name"),
		"isEnabled": IS_ENABLED or PROFILE_GROUP_INFO.get("isEnabled"),
		"manifestType": MANIFEST_TYPE or PROFILE_GROUP_INFO.get("manifestType"),
		"isDefaultGroup": IS_DEFAULT_GROUP or PROFILE_GROUP_INFO.get("isDefaultGroup"),
		"outputType": LIVE_OUTPUT_TYPE or PROFILE_GROUP_INFO.get("outputType"),
		"archiveOutputProfile": ARCHIVE_LIVE_OUTPUT_PROFILE or PROFILE_GROUP_INFO.get("archiveOutputProfile"),
		"outputProfiles": LIVE_OUTPUT_PROFILES or PROFILE_GROUP_INFO.get("outputProfiles")
	}

	if DEBUG:
		print(f"API_URL: {API_URL}\nMETHOD: PUT\nBODY: {json.dumps(BODY, indent=4)}")

	retries = 0
	while True:
		try:
			RESPONSE = requests.put(API_URL, headers=HEADERS, data=json.dumps(BODY))
	
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
				_api_exception_handler(RESPONSE, "Update Live Output Profile Group Failed")
	
		except:
			_api_exception_handler(RESPONSE, "Update Live Output Profile Group Failed")
	
	return RESPONSE.json()