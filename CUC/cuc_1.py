import os
import requests

# Variables to be updated based on your specifications
input_folder_path = "/path/to/your/input/folder"
api_key = "your_api_key"
api_base_url = "https://your-api-base-url.com"

# Iterate through all the folders in the input_folder_path
for folder_name in os.listdir(input_folder_path):
    # If it is a folder
    if os.path.isdir(os.path.join(input_folder_path, folder_name)):
        # Assuming the json file is named input.json
        json_file_path = os.path.join(input_folder_path, folder_name, "input.json")

        # Check if the json file exists
        if os.path.isfile(json_file_path):
            # Read the json file
            with open(json_file_path, "r") as file:
                json_data = file.read()

            # Prepare the headers
            headers = {
                "api_key": api_key,
                "Content-Type": "application/json"
            }

            # Prepare the data
            data = {
                "type": "VENDOR",
                "UserId": "206",
                "ProjectName": folder_name,
                "RefStyle": "none",
                "Json": json_data
            }

            # Send the POST request
            response = requests.post(
                f"{api_base_url}/path/to/your/input/endpoint",
                headers=headers,
                data=data
            )

            # Check the response
            if response.json() == {"Message": "Package received"}):
                print(f"Successfully uploaded input file for project {folder_name}")
            else:
                print(f"Failed to upload input file for project {folder_name}")
            continue
        else:
            print(f"Json file not found for project {folder_name}")
            continue

    # Get the status
    headers = {
        "api_key": api_key,
        "Content-Type": "application/json"
    }

    data = {
        "UserId": "206"
    }

    response = requests.post(
        f"{api_base_url}/path/to/your/status/endpoint",
        headers=headers,
        json=data
    )

    response_data = response.json()

    # Check the status
    if "output & report" in response_data:
        # Get the JobId of the output
        job_id = response_data["your_key_for_job_id"]

        # Download the file
        response = requests.get(
            f"{api_base_url}/path/to/your/download/endpoint/{job_id}",
            headers=headers
        )

        # Save the file
        with open(os.path.join(input_folder_path, folder_name, "output_folder", "your_file_name.extension"),
                  "wb") as file:
            file.write(response.content)

        print(f"Successfully downloaded output file for project {folder_name}")
    else:
        print(f"Output and report not available for project {folder_name}")