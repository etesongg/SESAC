import os
import sys
import requests
import cv2
import numpy as np
import json

def clova_face(filename):
    client_id = 'eIk2DWYQDZ7beiHuGdRe'
    client_secret = open('secret.txt', 'r').read()

    url = "https://openapi.naver.com/v1/vision/face" # 얼굴감지
    # url = "https://openapi.naver.com/v1/vision/celebrity" # 유명인 얼굴인식

    files = {'image': open(filename, 'rb')}
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }

    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)

    data = json.loads(response.text)
    return data

def my_opencv(filename):
    face_info = clova_face(filename)
    print(face_info)

    img_array = np.fromfile(filename, np.uint8)
    image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    for face in face_info['faces']:
        roi = face['roi']
        x, y, w, h = roi['x'], roi['y'], roi['width'], roi['height']

        gender = face['gender']['value']
        age = face['age']['value']
        emotion = face['emotion']['value']
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 3)

        cv2.putText(image, gender, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 1)
        cv2.putText(image, age, (x,y+h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 1)
        cv2.putText(image, emotion, (x,y+h*2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 1)

        

    # cv2.namedWindow("WindowName", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('WindowName', 500, 600)
    cv2.imshow('WindowName', image)
    # cv2.imshow('출력할창이름', image)
    cv2.waitKey(0)

if __name__ == "__main__":
    filename = 'images/정국_한소희.jpg'
    my_opencv(filename)