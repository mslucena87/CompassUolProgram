import boto3
from botocore.exceptions import NoCredentialsError
import pandas as pd

aws_access_key_id = 'ASIAY5VPO54KGU3F26M2'
aws_secret_access_key = '7vyGQQlDvpuxgCDrq1Mo4NZUrBzYzA/7++kiFdnr'
session_token = 'IQoJb3JpZ2luX2VjEKX//////////wEaCXVzLWVhc3QtMSJHMEUCIQDg3ifM1foojMeKAoEcZ8rWjKPQNJcWJXz9iV+1ypyjoAIgecdUMdSSYeA5aCxys9e2wFwrBVRVVeI2RxqiFG5PRBcqoQMIHhAAGgw2MTM0NzQ1NjE4MTIiDG1i8eZKaJHJY91sACr+AnsYw2J3CWlGvm2vOfK2di9qV8L1z270UH0D+rLCV8BLoANriIJG7znkv6A5oPBmeRglB8Z8pqDGyBfs6SBNscZHJgwVBxiE3lSfAGQa3daylUPJFyNojz3E6wDhrU7HN5nL9E03jrGB0GTPCfypGZhhSVG6gtZ8/L5pG5x1qo2EdHGFcj0gW6evG6WTUE8PMvyocmg58157ghCDsF0xAqFbGAlHrVSbLxFaN52sU75fKaLMDSzG/6i6tBKy4uOuHBnO0Af7i1X8P7qxbkg876SBxE/aFcrL9ahZeLyDq86+g7yuEFFjXAAksS0xdcmhEfbdUkmWjo8BfMhTAY4dACj5KoYrQRcjGqmwKkn8kRpoyW8im8hXchUvLfT2d3lOGDwaKHoZaTqCfDW1kHJgW3HJ8mBLIMQGW/3FUZ0bfTkK+rgL0cl5zKVYVEogNqRQyAvw2bXkgOZ/MY3/3ounZepVP4Ax9rnqCYSyN9ilaJbENxs7hzT5a0Gnn4OR1aUwvefdqwY6pgEYOA7CxktBd4e1rPqv1CuC7H/16NW2tvbbZSgeId9uxP7PId8j6Pl1ipTzojd+5VU5tS4jXBS5Wkx9UbR5hzIc8UBsnHiGvC6CbCgwJJSCh2aTLPKIp6EOtpir80nWZrPLKM5CBcwCGPNFzJ2zo5XYjQsbu/hK+wACXAHAFUB+5+pMwBnUk1nhQRubj8jOgfIgDdBafg/o+1VuhgY/1kkhBZrCbgca'
aws_region = 'us-east-1'
bucket_name = 'marcelabucket'

# def create_s3_bucket(bucket_name, region='us-east-1', access_key=None, secret_key=None, session_token=None):
#     # Create an S3 client with optional access key, secret key, and session token
#     session_credentials = {
#         'aws_access_key_id': access_key,
#         'aws_secret_access_key': secret_key,
#         'aws_session_token': session_token
#     }

#     s3 = boto3.client('s3', region_name=region, **session_credentials)

#     # Create a new S3 bucket
#     try:
#         s3.create_bucket(Bucket=bucket_name)
#         print(f"Bucket '{bucket_name}' created successfully.")
#     except NoCredentialsError:
#         print("Credentials not available.")

# create_s3_bucket(bucket_name, aws_region, aws_access_key_id, aws_secret_access_key, session_token)

s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=session_token,
                region_name=aws_region)

# Print the first few lines of the CSV files
print("Movies CSV Preview:")
with open(r'C:/Users/user/Projetos/CompassUolProgram/Sprint7/Exercícios/EtlParte1/FilmesESeries/movies.csv', 'r') as f_movies:
    for _ in range(5):
        print(f_movies.readline().strip())

print("\nSeries CSV Preview:")
with open(r'C:/Users/user/Projetos/CompassUolProgram/Sprint7/Exercícios/EtlParte1/FilmesESeries/series.csv', 'r') as f_series:
    for _ in range(5):
        print(f_series.readline().strip())


def upload_to_s3(file_path, key):
    try:
        s3_client.upload_file(file_path, bucket_name, key)
        print(f'Successfully uploaded {file_path} to {bucket_name}/{key}')
    except Exception as e:
        print(f'Error uploading {file_path} to {bucket_name}/{key}: {e}')


filmes_df = pd.read_csv(r'C:/Users/user/Projetos/CompassUolProgram/Sprint7/Exercícios/EtlParte1/FilmesESeries/movies.csv', sep='|')
series_df = pd.read_csv(r'C:/Users/user/Projetos/CompassUolProgram/Sprint7/Exercícios/EtlParte1/FilmesESeries/series.csv', sep='|')


upload_to_s3(r'C:/Users/user/Projetos/CompassUolProgram/Sprint7/Exercícios/EtlParte1/FilmesESeries/movies.csv', '/Raw/Local/CSV/Movies/2022/05/02/movies.csv')
upload_to_s3(r'C:/Users/user/Projetos/CompassUolProgram/Sprint7/Exercícios/EtlParte1/FilmesESeries/series.csv', '/Raw/Local/CSV/Series/2022/05/02/series.csv')
