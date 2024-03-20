import requests
import os

def upload_zip_to_postman(api_key):
    # Define the base URL for the POST request
    postman_url = 'https://qaconfirmplusapi.icodex.in/Package/status'

    # Authorization parameters
    headers = {
        'Authorization': f'API_KEY {api_key}'
    }

    # Define raw data to be sent
    raw_data = {
    "UserId":206
    }

    # Send POST request to Postman with raw data
    response = requests.post(postman_url, headers=headers, json=raw_data)

    if response.status_code == 201:
        print(f"File uploaded successfully: {response.text[:415]}")
    else:
        print(f"Failed to upload file. Error: {response.text}")


# Replace 'api_key' with your actual Postman API key
api_key = 'CUCCLI11UI#AB'

upload_zip_to_postman(api_key)
