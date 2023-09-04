import boto3

# AWS 기본 설정 후 버킷 목록 출력
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)