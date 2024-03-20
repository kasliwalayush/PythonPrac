import os
import shutil

def move_files_to_job_folder(job_id, destination_folder):
    # Replace 'Downloads' with the actual folder name containing the job ID folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    job_folder_path = os.path.join(downloads_folder, job_id)

    if os.path.exists(job_folder_path):
        # Move files to the specified destination folder
        input_folder = os.path.join(job_folder_path, "input")
        output_folder = os.path.join(job_folder_path, "output")

        # Destination directory for the job ID
        job_destination_path = os.path.join(destination_folder, job_id)

        # Create the job ID folder if it doesn't exist
        if not os.path.exists(job_destination_path):
            os.makedirs(job_destination_path)

        # Move input files to the job ID folder
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".zip") or file_name.endswith("article.json"):
                shutil.move(os.path.join(input_folder, file_name), os.path.join(job_destination_path, file_name))

        # Move output files to the output folder in the job ID folder
        output_destination = os.path.join(job_destination_path, "output")
        if not os.path.exists(output_destination):
            os.makedirs(output_destination)

        for file_name in os.listdir(output_folder):
            shutil.move(os.path.join(output_folder, file_name), os.path.join(output_destination, file_name))
    else:
        print(f"Job ID folder '{job_id}' not found in the Downloads folder.")

# Replace 'YOUR_JOB_ID' with the actual job ID
job_id = 'YOUR_JOB_ID'

# Replace '/path/to/destination' with the desired destination folder
destination_folder = '/path/to/destination'

move_files_to_job_folder(job_id, destination_folder)
