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
            link = movie.select_one('div > div.thumb_item > div.poster_info > a')
            rank = movie.select_one('div.thumb_item > div.poster_movie > span.rank_num')
            img_tag = movie.select_one('div.thumb_item > div.poster_movie ')
            if title_tag:
                movie_title = title_tag.text.strip()
                movie_grade = grade_tag.text.strip()
                movie_num = num_tag.text.strip().replace('%','')
                movie_url = link['href']
                movie_short = link.text.strip()
                rank = rank.text.strip()
                img = img_tag.img["src"]
                print(movie_title)
                print(movie_grade)
                print(movie_num)
                print(movie_url)
                print(movie_short)
                print(rank)
                print(img)

    # 포스터URL링크, 쇼트설명
    elif type == 'link':
        links = movie.select_one('div > div.thumb_item > div.poster_info > a')
        for link in links: 
            # movie_lilnk = requests.get('https://movie.daum.net/' + link['href'])
            
            print(link['href'], link.text.strip() )
            print('='*20)
    

    # # 쇼트설명(javascript로 되어 있어서 안 가져와짐)
    # elif type == 'short':
    #     links = soup.select('div > div.thumb_item > div.poster_info > a')
    #     for link in links: 
    #         movie_lilnk = requests.get('https://movie.daum.net/' + link['href'])
    #         soup = BeautifulSoup(movie_lilnk.text, 'html.parser')
    #         short = soup.select('.detail_basicinfo > .movie_summary > .info_desc > .desc_cont')
    #         print(short)
        
    
            
            
if __name__ == '__main__':
    get_daum_movie('movie_rank')
    # get_daum_movie('link')