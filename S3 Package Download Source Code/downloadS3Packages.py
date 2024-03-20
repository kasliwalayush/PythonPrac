import boto3
import os


def download_files_from_s3(bucket_name, job_id, destination_folder):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    # Search for the job ID folder in the 'packages' folder
    job_folder_prefix = f'packages/{job_id}/'

    for obj in bucket.objects.filter(Prefix=job_folder_prefix):
        if obj.key.endswith('.zip') or obj.key.endswith('article.json'):
            # Download the files
            bucket.download_file(obj.key, os.path.join(destination_folder, obj.key.split('/')[-1]))

    # Create a directory for the given job ID if it doesn't exist
    job_folder_path = os.path.join(destination_folder, job_id)
    if not os.path.exists(job_folder_path):
        os.makedirs(job_folder_path)

    # Move the downloaded files to the input folder of the job ID location
    os.rename(os.path.join(destination_folder, f'{job_id}.zip'), os.path.join(job_folder_path, f'{job_id}.zip'))
    os.rename(os.path.join(destination_folder, f'{job_id}article.json'),
              os.path.join(job_folder_path, f'{job_id}article.json'))

    # Download and store the output folder in the job ID location
    output_folder_prefix = f'packages/{job_id}/output/'
    for obj in bucket.objects.filter(Prefix=output_folder_prefix):
        bucket.download_file(obj.key, os.path.join(job_folder_path, 'output', obj.key.split('/')[-1]))


# Replace with your AWS credentials or use environment variables/credentials file for security
aws_access_key_id = 'Access_key'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION'

bucket_name = 'Bucket Name'
job_id = 'JodID Here'
destination_folder = 'Path Here'  # Replace with your desired destination folder

# Set AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = aws_access_key_id
os.environ['AWS_SECRET_ACCESS_KEY'] = aws_secret_access_key
os.environ['AWS_DEFAULT_REGION'] = region_name

download_files_from_s3(bucket_name, job_id, destination_folder)