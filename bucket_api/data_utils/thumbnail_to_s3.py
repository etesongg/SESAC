import boto3
import requests
import os

def thumbnail_to_s3(thumbnail_img):
    # S3 클라이언트 생성
    s3_client = boto3.client('s3')
    # 업로드할 이미지 파일과 버킷 이름 설정
    filename = image_download(thumbnail_img)  # 업로드할 이미지 파일 경로
    bucket_name = 'mytest-song'  
    file_key = filename
    # file_key = 'thumbnail_imgs/' + filename # 이렇게 하면 s3에도 thumbnail_imgs폴더에 저장되는데 object_url에 thumbnail_imgs/thumbnail_imgs\image_1.jpg 라고 저장됨

    # 이미지를 S3 버킷에 업로드
    s3_client.upload_file(filename, bucket_name, file_key)

    # S3 객체 URL 생성
    object_url = f"https://{bucket_name}.s3.amazonaws.com/{file_key}"
    
    return object_url

def image_download(thumbnail_img):
    image_url =thumbnail_img

    # 이미지를 저장할 로컬 디렉토리 경로 지정
    local_directory = 'thumbnail_imgs'

    # 이미지 다운로드
    response = requests.get(image_url)

    # 이미지 파일 이름 자동 생성 (예: 'image_1.jpg', 'image_2.jpg', 등)
    file_name = os.path.join(local_directory, f'image_{len(os.listdir(local_directory)) + 1}.jpg')
    # 이미지를 파일로 저장
    with open(file_name, 'wb') as f:
        f.write(response.content)
    
    return file_name