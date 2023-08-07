import requests
from bs4 import BeautifulSoup

def get_naver_sportnews():
    data = requests.get('https://sports.news.naver.com/index')
    soup = BeautifulSoup(data.text, 'html.parser')

    # print(soup)
    news = soup.select('.today_list > li')
    # print(len(news))

    naver_news_url = 'https://sports.news.naver.com/'
    for n in news:
        a_tag = n.select_one('a')
        # print(a_tag['title'])
        print(naver_news_url+a_tag['href'])

        # title = n.select_one('.title')
        # print(title.text)

        # strong = n.select_one('strong')
        # print(strong.text)

def get_naver_land(type):
    data = requests.get('https://land.naver.com/news/')
    soup = BeautifulSoup(data.text, 'html.parser')

    if type == 'headline':
        # 1. 분야별 헤드라인 정보 가져오기
        # headlines = soup.select('.section_group.NE\=a\:chl > ul > li')
        # for headline in headlines:
        #     a_tags = headline.select('a')
        #     print(a_tags[0].text + a_tags[1].text)

        content = soup.select_one('#content')
        section_group = content.select_one('.section_group')
        list_type = section_group.select('.list_type > li')
        # for news in list_type:
        #     a_tags = news.select('a')
        #     print(f'{a_tags[0].text} {a_tags[1].text}')

        # 미션3. 헤드라인 기사의 본문 내용중 text 부분을 다 가져온다.
        for news in list_type:
            a_tags = news.select('a')
            link = a_tags[1]['href']
            news_link = requests.get('https://land.naver.com' + link)
            soup = BeautifulSoup(news_link.text, 'html.parser')
            content = soup.select('#container > #content > #articleBody')
            print(content)
            
            # 다시 해보기
            # news_content = soup.select_one('.news_end')
            # if news_content:
            #     start_span = news_content.find('span')
            #     end_p = news_content.find('p', class_='source')
            #     if start_span and end_p:
            #         content = start_span.next_element
            #         while content and content != end_p:
            #             if isinstance(content, str) and content.strip():
            #                 print(content.strip())
            #             content = content.next_element
            # print('-'*20)
        
    elif type == 'trend':
        # 2. 동향보고서 내용 가져오기
        reports = soup.select('.section_group.NE\=a\:trd > ul > li')
        for report in reports:
            print(report.text.strip())
    else:
        print('Unknown type')



    

if __name__ == '__main__':
    # get_naver_sportnews()
    # get_naver_land('headline')
    get_daum_movie()

