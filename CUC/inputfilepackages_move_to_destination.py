import os
import shutil

def move_input_files_to_specific_folder(root_directory, destination_folder):
    for root, dirs, files in os.walk(root_directory):
        for dir_name in dirs:
            input_folder = os.path.join(root, dir_name, "input")
            if os.path.exists(input_folder):
                for file in os.listdir(input_folder):
                    if file.endswith('.json'):
                        source_file_path = os.path.join(input_folder, file)
                        destination_file_path = os.path.join(destination_folder, file)
                        shutil.copy(source_file_path, destination_file_path)
                        print(f"Copied {file} to {destination_folder}")

# Replace 'ROOT_DIRECTORY_PATH' with the path to your root directory
root_directory_path = 'H:\\iCodex\\eAssistant Packages\\TNQ'

# Replace 'SPECIFIC_INPUT_FOLDER_PATH' with the path to your specific 'input' folder
specific_input_folder_path = 'H:\\Onedrive\\Desktop\\inptut_file'

move_input_files_to_specific_folder(root_directory_path, specific_input_folder_path)
