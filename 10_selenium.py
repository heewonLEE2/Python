# 네이버 웹툰 댓글 크롤링
# https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# Chrome 창이 바로 받혀서 sleep을 주어서 10초 후에 닫힌다.
driver = webdriver.Chrome()
driver.get('https://comic.naver.com/webtoon/detail?titleId=834886&no=53&week=mon')

# selenium에서 가져온 html 객체를 BeautifulSoup에 넣는다.
soup = BeautifulSoup(driver.page_source)

# soup에 있는 html 객체에서 'span' 을 찾아서 속성 'class' : "u_cbox_contents" 를 찾는다
comment_area = soup.find_all('span',{"class":"u_cbox_contents"})
print('********* 베스트 댓글 **********')
# print(comment_area[0].text)
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print(' - ' * 20)

# xPath 개발자 도구에 들어가서 copy 클릭을 하면 있다.
# /html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]
driver.find_element('xpath','/html/body/div[1]/div[5]/div/div/div[4]/div[1]/div[3]/div/div/div[4]/div[1]/div/ul/li[2]/a/span[2]').click()

time.sleep(2)

# 전체 댓글과 BEST 댓글이 span 태그안에 class가 같아서 뒤에 내용을 그대로 씀
soup = BeautifulSoup(driver.page_source)
comment_area = soup.find_all('span',{"class":"u_cbox_contents"})
print('********* 전체댓글 **********')
for i in range(len(comment_area)):
    comment = comment_area[i].text.strip()
    print(comment)
    print(' - ' * 20)

time.sleep(10)