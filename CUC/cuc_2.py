import requests
import os
import time


# Function to send input file and get status
def send_input_file_and_get_status(input_file_path, headers, input_api_url, status_api_url, download_api_url):
    job_id = os.path.basename(os.path.dirname(input_file_path))  # Extract JobID from the input file's path
    project_name = job_id  # Use JobID as project name

    payload = {
        'type': 'VENDOR',
        'UserId': 206,
        'ProjectName':  {job_id},
        'RefStyle': 'none'
    }

    files = {'Json': open(input_file_path, 'rb')}

    input_response = requests.post(input_api_url, headers=headers['input'], data=payload, files=files)
    input_json = input_response.json()

    if input_json.get('isSuccess') == 'true' and input_json.get('ReferenceNumber'):
        start_time = time.time()
        while time.time() - start_time <= 300:  # Limit status check to 5 minutes (300 seconds)
            status_response = requests.post(status_api_url, headers=headers['status'], json={'UserId': 206})
            status_json = status_response.json()

            for item in status_json.get('dtoStatus', []):
                if item.get('ProjectName') == project_name and item.get('Status') == 'Output & Report':
                    new_job_id = item.get('JobId')
                    download_response = requests.get(download_api_url.format(new_job_id), headers=headers['download'])
                    if download_response.status_code == 200:
                        output_folder = os.path.join(os.path.dirname(input_file_path), 'output')
                        os.makedirs(output_folder, exist_ok=True)
                        output_file_path = os.path.join(output_folder, f'{new_job_id}.json')
                        with open(output_file_path, 'w') as output_file:
                            output_file.write(download_response.text)
                        print(f"Output downloaded successfully to: {output_file_path}")

                        # Store in the output folder within the JobID folder
                        output_job_folder = os.path.join(os.path.dirname(input_file_path), 'output')
                        os.makedirs(output_job_folder, exist_ok=True)
                        output_job_file_path = os.path.join(output_job_folder, f'{new_job_id}_output.json')
                        with open(output_job_file_path, 'w') as output_job_file:
                            output_job_file.write(download_response.text)
                        print(f"Output copied to: {output_job_file_path}")
                        return True
            time.sleep(10)  # Check status every 10 seconds

    print("Process unsuccessful or timed out.")
    return False


# Replace with your API endpoints and folder location
input_api_endpoint = 'https://qaconfirmplusapi.icodex.in/confirmplus/input/V2/files'
status_api_endpoint = 'https://qaconfirmplusapi.icodex.in/Package/status'
download_api_endpoint = 'https://qaconfirmplusapi.icodex.in/file/downloadjson/{new_job_id}/FinalDoc_MSReport?'

folder_location = 'H:\\iCodex\\eAssistant Packages\\TNQ'

# Define headers for input, status, and download APIs
headers = {
    'input': {
        'Authorization': 'eAssistantXApiKey',
        'Another-Header': 'iCod0001^YHN7ujmL1KGBO1UI#AB'  # Add other input headers if needed
    },
    'status': {
        'Authorization': 'eAssistantXApiKey',
        'Another-Header': 'CUCCLI11UI#AB'  # Add other status headers if needed
    },
    'download': {
        'Authorization': 'eAssistantXApiKey',
        'Another-Header': 'CUCCLI11UI#AB'  # Add other download headers if needed
    }
}

# Iterate through all folders in the specified directory
for folder in os.listdir(folder_location):
    folder_path = os.path.join(folder_location, folder)
    if os.path.isdir(folder_path):
        input_folder = os.path.join(folder_path, 'input')
        if os.path.exists(input_folder):
            input_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if
                           file.endswith('.json')]
            for input_file in input_files:
                print(f"Processing file: {input_file}")
                success = send_input_file_and_get_status(input_file, headers, input_api_endpoint, status_api_endpoint,
                                                         download_api_endpoint)
                if success:
                    print("Processing of this file completed successfully.")
                else:
                    print("Processing of this file was unsuccessful.")
