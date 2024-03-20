import requests
import os

def upload_zip_to_postman(job_id, api_key, zip_file_path):
    # Define the base URL for the POST request
    postman_url = 'https://qaconfirmplusapi.icodex.in/confirmplus/input/V2/files'

    # Authorization parameters
    headers = {
        'Authorization': f'API_KEY {api_key}',
        'type': 'VENDOR',
        'UserId': '206',
        'ProjectName': f'{job_id}',
        'RefStyle': 'None'
    }

    # Check if the file exists before attempting to open it
    if not os.path.exists(zip_file_path):
        print(f"File '{zip_file_path}' does not exist for Job ID: {job_id}")
        return

    files = {
        'zip': open(zip_file_path, 'rb')
    }

    # Send POST request to Postman
    response = requests.post(postman_url, headers=headers, files=files)

    if response.status_code == 201:
        print(f"File uploaded successfully for Job ID {job_id}: {response.text}")
    else:
        print(f"Failed to upload file for Job ID {job_id}. Error: {response.text}")


# Replace 'api_key' with your actual Postman API key
api_key = 'iCod0001^YHN7ujmL1KGBO1UI#AB'

# Replace the directory path where your zip files are located
directory_path = 'H:\\iCodex\\eAssistant Packages\\testTNQ\\'

# Iterate through all files in the directory and upload zip files
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('.zip'):
            job_id = os.path.basename(root)  # Using directory name as job_id
            file_path = os.path.join(root, file)
            upload_zip_to_postman(job_id, api_key, file_path)
