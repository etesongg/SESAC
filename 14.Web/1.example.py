import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.pythonscraping.com/pages/page3.html')


soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

gifts = soup.select('#giftList > tr ')
print(gifts)

my_gifts = gifts[1:]
print(len(my_gifts))

for g in my_gifts:
    print(g)
    tds = g.select('td')
    # spans = g.select('td > span')
    # print(spans)
    print(f'title: {tds[0].text.strip()}, price: {tds[2].text.strip()}')
    print(f'PIC: {tds[3].img["src"]}')
