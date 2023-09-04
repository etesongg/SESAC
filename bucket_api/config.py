# Flask 애플리케이션 설정
DEBUG = True
SECRET_KEY = 'sesac-totay_exhibition-team3'
SQLALCHEMY_DATABASE_URI = 'sqlite:///today-exhibition.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
PORT = 8000

# URL 설정
LOCAL_HOST_URL = "http://127.0.0.1:" + str(PORT)
NAVER_CALLBACK_URL = LOCAL_HOST_URL + "/login/callback/naver"
KAKAO_CALLBACK_URL = LOCAL_HOST_URL + "/login/callback/kakao"