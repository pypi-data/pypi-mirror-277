from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _create_live_output_profile_group(self, AUTH_TOKEN, URL, NAME, IS_ENABLED, MANIFEST_TYPE, IS_DEFAULT_GROUP, LIVE_OUTPUT_TYPE, ARCHIVE_LIVE_OUTPUT_PROFILE, LIVE_OUTPUT_PROFILES, DEBUG):

	API_URL = f"{URL}/api/liveOutputProfileGroup"

	HEADERS = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {AUTH_TOKEN}"
	}

	BODY = {
		"name": NAME,
		"enabled": IS_ENABLED,
		"manifestType": MANIFEST_TYPE,
		"isDefaultGroup": IS_DEFAULT_GROUP,
		"outputType": LIVE_OUTPUT_TYPE,
		"archiveOutputProfile": ARCHIVE_LIVE_OUTPUT_PROFILE,
		"outputProfiles": LIVE_OUTPUT_PROFILES
	}
	if DEBUG:
		print(f"API_URL: {API_URL}\nMETHOD: POST\nBODY: {json.dumps(BODY, indent=4)}")

	retries = 0
	while True:
		try:
			RESPONSE = requests.post(API_URL, headers=HEADERS, data=json.dumps(BODY, indent=4))

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
				_api_exception_handler(RESPONSE, "Create Live Output Profile Group Failed")

		except:
			_api_exception_handler(RESPONSE, "Create Live Output Profile Group Failed")
			
	return RESPONSE.json()