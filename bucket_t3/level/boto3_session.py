import boto3
from utils import load_secrets

# AWS S3 자격 증명 정보를 읽어와 AWS S3 서비스에 연결하고, 연결된 서비스로부터 S3 버킷 목록을 가져와서 각 버킷의 이름을 출력
secrets = load_secrets()
aws_s3_key = secrets["database"]

session = boto3.Session(
    profile_name='etesong0114@gmail.com',
    aws_access_key_id = aws_s3_key["aws_s3_Access_key"],
    aws_secret_access_key = aws_s3_key["aws_s3_Secret_access_key"],
    region_name="us-east-1"
)

s3 = session.resource('s3')

for bucket in s3.buckets.all(): 
	print(bucket.name)