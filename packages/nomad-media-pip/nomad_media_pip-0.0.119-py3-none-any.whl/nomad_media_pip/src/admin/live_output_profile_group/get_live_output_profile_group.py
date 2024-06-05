from nomad_media_pip.src.exceptions.api_exception_handler import _api_exception_handler

import requests, json, time
MAX_RETRIES = 2

def _get_live_output_profile_group(self, AUTH_TOKEN, URL, LIVE_OUTPUT_PROFILE_GROUP_ID, DEBUG):

	API_URL = f"{URL}/api/liveOutputProfileGroup/{LIVE_OUTPUT_PROFILE_GROUP_ID}"

	HEADERS = {
		"Content-Type": "application/json",
		"Authorization": f"Bearer {AUTH_TOKEN}"
	}

	if DEBUG:
		print(f"API_URL: {API_URL}\nMETHOD: GET")

	retries = 0
	while True:
		try:
			RESPONSE = requests.get(API_URL, headers=HEADERS)
	
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
				_api_exception_handler(RESPONSE, "Get Live Output Profile Group Failed")
	
		except:
			_api_exception_handler(RESPONSE, "Get Live Output Profile Group Failed")
			
	return RESPONSE.json()