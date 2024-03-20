import requests
import os

def upload_zip_to_postman(job_id, api_key):
    # Define the base URL for the POST request
    postman_url = 'https://qaconfirmplusapi.icodex.in/confirmplus/input/V2/files'

    # Authorization parameters
    headers = {
        'Authorization': f'API_KEY {api_key}',
        'type': 'VENDOR',
        'UserId': '206',
        'ProjectName': job_id,  # Use job_id as ProjectName
        'RefStyle': 'None'
    }

    # Path to the 'input' folder of the Job ID folder
    input_folder_path = f'H:\\iCodex\\eAssistant Packages\\TNQ\\{job_id}\\input'

    # Check if the 'input' folder exists for the job ID
    if not os.path.exists(input_folder_path) or not os.path.isdir(input_folder_path):
        print(f"Input folder not found for Job ID: {job_id}")
        return

    # Find the first zip file within the 'input' folder
    zip_files = [f for f in os.listdir(input_folder_path) if f.endswith('.zip')]
    if not zip_files:
        print(f"No zip file found in the input folder for Job ID: {job_id}")
        return

    zip_file_path = os.path.join(input_folder_path, zip_files[0])

    # Send POST request to Postman
    with open(zip_file_path, 'rb') as file:
        files = {'zip': file}
        response = requests.post(postman_url, headers=headers, files=files)

    if response.status_code == 201:
        print(f"File uploaded successfully for Job ID {job_id}: {response.text}")
    else:
        print(f"Failed to upload file for Job ID {job_id}. Error: {response.text}")


# Replace 'api_key' with your actual Postman API key
api_key = 'iCod0001^YHN7ujmL1KGBO1UI#AB'

# Replace the directory path where your job ID folders are located
root_directory = 'H:\\iCodex\\eAssistant Packages\\testTNQ\\'

# Iterate through all job ID folders and upload zip files
for job_folder in os.listdir(root_directory):
    job_folder_path = os.path.join(root_directory, job_folder)
    if os.path.isdir(job_folder_path):
        upload_zip_to_postman(job_folder, api_key)
