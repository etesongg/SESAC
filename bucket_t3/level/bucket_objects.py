import boto3

s3 = boto3.resource('s3')

BUCKET_NAME = "mytest-song"

bucket = s3.Bucket(BUCKET_NAME)
print(bucket)

for obj in bucket.objects.all():
    print(obj)
    print(obj.key)