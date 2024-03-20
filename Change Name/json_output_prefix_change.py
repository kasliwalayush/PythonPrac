# Rename multiple file at a time using loop

import os

def rename_output_json_files(root_folder):
    for foldername, subfolders, filenames in os.walk(root_folder):
        if os.path.basename(foldername) == 'output':
            # Get the path of the 'output' folder
            output_folder = foldername

            # Get the parent folder (jobid folder)
            jobid_folder = os.path.dirname(output_folder)

            # Check if 'output' folder contains a JSON file
            output_files = [file for file in filenames if file.endswith('.json')]
            if len(output_files) == 1:
                # Get the JSON file name
                json_file = output_files[0]

                # Generate the new filename with the 'EA' prefix
                new_filename = 'EA_' + json_file

                # Get the full path of the JSON file
                file_path = os.path.join(output_folder, json_file)

                # Rename the JSON file
                os.rename(file_path, os.path.join(output_folder, new_filename))

# Replace 'root_folder_path' with the path to your main directory containing folders
root_folder_path = 'Path Here'

# Call the function to rename JSON files in the 'output' subfolder within each 'jobid' folder
rename_output_json_files(root_folder_path)
