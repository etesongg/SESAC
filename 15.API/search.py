import os
import sys
import urllib.request
import json

client_id = 'eIk2DWYQDZ7beiHuGdRe'
client_secret = open('secret.txt', 'r').read()

text = "반갑습니다"
encText = urllib.parse.quote(text)
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)





