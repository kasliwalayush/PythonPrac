import boto3
import os
import shutil


def download_files_from_s3(bucket_name, job_id, destination_folder):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    input_folder_prefix = f'TNQ/{job_id}/input/'
    output_folder_prefix = f'TNQ/{job_id}/output/'

    # Download .zip and .json files from input folder
    for obj in bucket.objects.filter(Prefix=input_folder_prefix):
        if obj.key.endswith('.zip') or obj.key.endswith('article.json'):
            bucket.download_file(obj.key, os.path.join(destination_folder, obj.key.split('/')[-1]))

    # Download .json files from output folder
    for obj in bucket.objects.filter(Prefix=output_folder_prefix):
        if obj.key.endswith('.json'):
            bucket.download_file(obj.key, os.path.join(destination_folder, obj.key.split('/')[-1]))


def move_files_to_job_folder(job_id, destination_folder):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    job_folder_path = os.path.join(downloads_folder, job_id)

    if os.path.exists(job_folder_path):
        input_folder = os.path.join(job_folder_path, "input")
        output_folder = os.path.join(job_folder_path, "output")
        job_destination_path = os.path.join(destination_folder, job_id)

        if not os.path.exists(job_destination_path):
            os.makedirs(job_destination_path)

        for file_name in os.listdir(input_folder):
            if file_name.endswith(".zip") or file_name.endswith("article.json"):
                shutil.move(os.path.join(input_folder, file_name), os.path.join(job_destination_path, file_name))

        output_destination = os.path.join(job_destination_path, "output")
        if not os.path.exists(output_destination):
            os.makedirs(output_destination)

        for file_name in os.listdir(output_folder):
            if file_name.endswith(".json"):
                shutil.move(os.path.join(output_folder, file_name), os.path.join(output_destination, file_name))
    else:
        print(f"Job ID folder '{job_id}' not found in the Downloads folder.")


def download_and_move_files_from_job_ids(bucket_name, file_path, destination_folder):
    with open(file_path, 'r') as file:
        job_ids = file.read().splitlines()

    for job_id in job_ids:
        download_files_from_s3(bucket_name, job_id, destination_folder)
        move_files_to_job_folder(job_id, destination_folder)


# AWS credentials and bucket name
aws_access_key_id = 'Key_Id'
aws_secret_access_key = 'Key'
region_name = 'Region'
bucket_name = 'Bucket Name'

# Replace '/path/to/job_ids.txt' with the path to your job IDs file
job_ids_file = 'Path Here'

# Replace '/path/to/destination' with the desired destination folder
destination_folder = 'Path Here'

# Set AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
os.environ['AWS_DEFAULT_REGION'] = region_name

download_and_move_files_from_job_ids(bucket_name, job_ids_file, destination_folder)
