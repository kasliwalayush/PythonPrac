import os

def rename_json_files(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        if os.path.basename(foldername) in ['input', 'output']:
            # Get the path of the 'input' or 'output' folder
            target_folder = foldername

            # Get the parent folder (jobid folder)
            jobid_folder = os.path.dirname(target_folder)

            # Check if 'input' or 'output' folder contains a JSON file
            json_files = [file for file in filenames if file.endswith('.json')]
            if len(json_files) == 1:
                # Get the JSON file name
                json_file = json_files[0]

                # Generate the new filename with the 'EA' prefix
                new_filename = 'EA' + json_file

                # Get the full path of the JSON file
                file_path = os.path.join(target_folder, json_file)

                # Rename the JSON file
                os.rename(file_path, os.path.join(target_folder, new_filename))

# Replace 'root_folder_path' with the path to your main directory containing folders
root_folder_path = 'Path Here'

# Call the function to rename JSON files in the 'input' and 'output' subfolders within each 'jobid' folder
rename_json_files(root_folder_path)
