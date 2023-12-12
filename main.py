import boto3
import pandas as pd

aws_access_key_id = 'ASIAY5VPO54KGU3F26M2'
aws_secret_access_key = '7vyGQQlDvpuxgCDrq1Mo4NZUrBzYzA/7++kiFdnr'
session_token = 'IQoJb3JpZ2luX2VjEKX//////////wEaCXVzLWVhc3QtMSJHMEUCIQDg3ifM1foojMeKAoEcZ8rWjKPQNJcWJXz9iV+1ypyjoAIgecdUMdSSYeA5aCxys9e2wFwrBVRVVeI2RxqiFG5PRBcqoQMIHhAAGgw2MTM0NzQ1NjE4MTIiDG1i8eZKaJHJY91sACr+AnsYw2J3CWlGvm2vOfK2di9qV8L1z270UH0D+rLCV8BLoANriIJG7znkv6A5oPBmeRglB8Z8pqDGyBfs6SBNscZHJgwVBxiE3lSfAGQa3daylUPJFyNojz3E6wDhrU7HN5nL9E03jrGB0GTPCfypGZhhSVG6gtZ8/L5pG5x1qo2EdHGFcj0gW6evG6WTUE8PMvyocmg58157ghCDsF0xAqFbGAlHrVSbLxFaN52sU75fKaLMDSzG/6i6tBKy4uOuHBnO0Af7i1X8P7qxbkg876SBxE/aFcrL9ahZeLyDq86+g7yuEFFjXAAksS0xdcmhEfbdUkmWjo8BfMhTAY4dACj5KoYrQRcjGqmwKkn8kRpoyW8im8hXchUvLfT2d3lOGDwaKHoZaTqCfDW1kHJgW3HJ8mBLIMQGW/3FUZ0bfTkK+rgL0cl5zKVYVEogNqRQyAvw2bXkgOZ/MY3/3ounZepVP4Ax9rnqCYSyN9ilaJbENxs7hzT5a0Gnn4OR1aUwvefdqwY6pgEYOA7CxktBd4e1rPqv1CuC7H/16NW2tvbbZSgeId9uxP7PId8j6Pl1ipTzojd+5VU5tS4jXBS5Wkx9UbR5hzIc8UBsnHiGvC6CbCgwJJSCh2aTLPKIp6EOtpir80nWZrPLKM5CBcwCGPNFzJ2zo5XYjQsbu/hK+wACXAHAFUB+5+pMwBnUk1nhQRubj8jOgfIgDdBafg/o+1VuhgY/1kkhBZrCbgca'
aws_region = 'us-east-1'
bucket_name = 'marcelabucket'

s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=session_token,
                region_name=aws_region)


def upload_to_s3(file_path, key):
    try:
        df = pd.read_csv(file_path, sep='|', low_memory=False)
        csv_buffer = df.to_csv(index=False, sep='|').encode()

        s3_client.put_object(Body=csv_buffer, Bucket=bucket_name, Key=key)
        print(f'Successfully uploaded {file_path} to {bucket_name}/{key}')
    except Exception as e:
        print(f'Error uploading {file_path} to {bucket_name}/{key}: {e}')


upload_to_s3(r'./data/movies.csv', 'Raw/Local/CSV/Movies/2022/05/02/movies.csv')
upload_to_s3(r'./data/series.csv', 'Raw/Local/CSV/Series/2022/05/02/series.csv')
