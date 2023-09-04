#### 정책 버전2(boto3_resource.py)

 - S3 버킷 목록을 나열하고, 버킷 위치 가져오는 데 필요한 권한 제공

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        }
    ]
}
```

<hr>

#### 정책 버전3(bucket_objects.py)

 - S3 버킷의 객체 목록 보기 권한 추가
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::my-bucket-name",  // 본인의 버킷 이름으로 변경
                "arn:aws:s3:::my-bucket-name/*" // 본인의 버킷 이름으로 변경
            ]
        }
    ]
}
```

<hr>

#### 정책 버전3(bucket_objects.py)

 - S3 버킷의 객체 목록 보기 권한 추가

```
			"Effect": "Allow",
			"Action": [
				"s3:ListBucket",
				"s3:GetObject",
				"s3:PutObject",    // 업로드 권한 추가
                "s3:PutObjectAcl" // ACL 수정 권한 추가
			],
```

