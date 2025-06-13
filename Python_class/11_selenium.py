import time
from selenium import webdriver
from bs4 import BeautifulSoup

# name = 호텔 이름, ulr = 그 호텔의 url
def crawl_yanolja_reviews(name, url):
    review_list = []
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)

    scroll_count = 3
    for i in range(scroll_count):
        # execute_script() : JS 코드를 사용할 수 있게 해줌
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
    # 끝까지 내린 상태에서의 html을 가져온다.
    soup = BeautifulSoup(driver.page_source)

    # 개발자 도구를 열어서 copy에서 selector를 가져옴 뒤에 child ntn 애들은 지워주면
    # 특정 div 만 가져오는게 아니라 다 가져올 수 있다. 
    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')
    # p 태그의 주소 child :ntn of 를 지워야 공통으로 뽑을 수 있음
    # #__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p

    for i in range(len(review_containers)):
       # print(i)
        # print(review_text, date)
        # print(review_empty_stars)
        review_text = review_containers[i].find('p', class_='content-text').text
        date = review_date[i].text
        review_empty_stars = review_containers[i].find_all('path',{'fill-rule':'evenodd'})
        stars = 5 - len(review_empty_stars)
        # review_dict 안에 데이터를 담기
        review_dict = {
            'review' : review_text,
            'star' : stars,
            'date' : date
        }
        # list에 dict을 담고 아래에서 list 출력
        review_list.append(review_dict)

    print(review_list)
    time.sleep(10)

crawl_yanolja_reviews('라발스 호텔 부산','https://nol.yanolja.com/reviews/domestic/3020201')