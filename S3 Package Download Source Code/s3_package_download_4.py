import boto3
import os


def download_files_from_s3(bucket_name, job_id, destination_folder):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    input_folder_prefix = f'TNQ/{job_id}/input/'
    output_folder_prefix = f'TNQ/{job_id}/output/'

    # Download .zip and "article.json" files from input folder
    for obj in bucket.objects.filter(Prefix=input_folder_prefix):
        if obj.key.endswith('.zip') or (obj.key.endswith('article.json') and input_folder_prefix in obj.key):
            bucket.download_file(obj.key, os.path.join(destination_folder, job_id, 'input', obj.key.split('/')[-1]))

    # Download "article.json" files from output folder
    for obj in bucket.objects.filter(Prefix=output_folder_prefix):
        if obj.key.endswith('article.json') and output_folder_prefix in obj.key:
            bucket.download_file(obj.key, os.path.join(destination_folder, job_id, 'output', obj.key.split('/')[-1]))


def download_and_move_files_from_job_ids(bucket_name, file_path, destination_folder):
    with open(file_path, 'r') as file:
        job_ids = file.read().splitlines()

    for job_id in job_ids:
        job_destination_path = os.path.join(destination_folder, job_id)
        if not os.path.exists(job_destination_path):
            os.makedirs(os.path.join(job_destination_path, 'input'))
            os.makedirs(os.path.join(job_destination_path, 'output'))

        download_files_from_s3(bucket_name, job_id, destination_folder)


# AWS credentials and bucket name
# Set your credentials or use a different method to set them securely
aws_access_key_id = 'Key_ID'
aws_secret_access_key = 'key'
region_name = 'Region'
bucket_name = 'Bucket Name'

# Set AWS credentials - replace with your own method of providing credentials securely
os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
os.environ['AWS_DEFAULT_REGION'] = region_name

# Replace '/path/to/job_ids.txt' with the path to your job IDs file
job_ids_file = 'Path Here'

# Replace '/path/to/destination' with the desired destination folder
destination_folder = 'Path Here'

download_and_move_files_from_job_ids(bucket_name, job_ids_file, destination_folder)
