import json
import requests


# Define the URL and payload data
def translate(text):
    url = "https://translation-api.translate.com/translate/v1/mt"
    data = {"source_language": "en", "translation_language": "ar", "text": text}

    # Define headers
    headers = {
        "accept": "*/*",
        "x-api-key": "16502a6ae20429",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRF-TOKEN": "",
    }

    # Make the POST request
    response = requests.request("POST", url, data=data, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the response content
        return json.loads(response.text).get("translation")
    else:
        return f"Request failed with status code {response.status_code}"
