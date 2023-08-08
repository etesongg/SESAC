import requests
from bs4 import BeautifulSoup

def get_daum_movie(type):
    data = requests.get('https://movie.daum.net/ranking/reservation')
    soup = BeautifulSoup(data.text, 'html.parser')
    # 다음영화랭킹(제목/평점/예매율)
    if type == 'movie_rank':
        movies = soup.select('#mainContent > div > div.box_ranking > ol > li')
        for movie in movies:
            title_tag = movie.select_one('div > div.thumb_cont > strong')
            grade_tag = movie.select_one('div > div.thumb_cont > span.txt_append > span:nth-child(1) > span')
            num_tag = movie.select_one('div.thumb_cont > span.txt_append > span:nth-child(2) > span')
            if title_tag:
                movie_title = title_tag.text.strip()
                movie_grade = grade_tag.text.strip()
                movie_num = num_tag.text.strip()
                print(f'{movie_title}, {movie_grade}, {movie_num}')

    # 포스터URL링크, 쇼트설명
    elif type == 'link':
        links = soup.select('div > div.thumb_item > div.poster_info > a')
        for link in links: 
            # movie_lilnk = requests.get('https://movie.daum.net/' + link['href'])
            print(link['href'], link.text.strip() )
            print('='*20)
    
             
            
if __name__ == '__main__':
    get_daum_movie('movie_rank')
    # get_daum_movie('link')