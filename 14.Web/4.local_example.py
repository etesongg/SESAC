# request로 가져오면 그 사이트에 부하를 줄 수 있기때문에 로컬에서 html코드를 가져와서 하기

from bs4 import BeautifulSoup

html = '''
<html>
<body>
  <div class="content">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </ul>
  </div>
  <div class="sidebar">
    <h2>Sidebar Title</h2>
    <p>Sidebar content</p>
  </div>
</body>
</html>
'''

soup = BeautifulSoup(html, 'html.parser')
sidebar_div = soup.find('div', class_='sidebar')
print(sidebar_div)
sidebar_div = soup.select('.sidebar')
print(sidebar_div)
print("-"*20)
p_tags_in_sidebar = sidebar_div.find_all('p')
for p_tag in p_tags_in_sidebar:
    print(p_tag.get_text())
print("-"*20)
p_tags_in_sidebar = soup.find_all('p')
for p_tag in p_tags_in_sidebar:
    print(p_tag.get_text())

