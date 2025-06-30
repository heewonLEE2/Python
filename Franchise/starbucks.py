import re
import time
import pandas as pd
from selenium import webdriver
# 바로 위에서 실행한 selenium 안에 있는 webdriver 안에 .ActionChains
from selenium.webdriver import ActionChains
# CSS Selector 등 으로 element들을 찾을 수 있게 해주는 By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def fetch_starbucks():
    starbucks_url = "https://www.starbucks.co.kr/index.do"
    driver = webdriver.Chrome()
    driver.maximize_window() # 화면 최대화
    driver.get(starbucks_url)
    time.sleep(1)

    # 여러 액션을 연결해서 사용
    action = ActionChains(driver)
    first_tag = driver.find_element(By.CSS_SELECTOR, "#gnb > div > nav > div > ul > li.gnb_nav03 > h2 > a")
    second_tag = driver.find_element(By.CSS_SELECTOR, "#gnb > div > nav > div > ul > li.gnb_nav03 > div > div > div > ul:nth-child(1) > li:nth-child(3) > a")
    # 마우스를 얹어라 perform()이 실행 하라는 메소드 그 전에는 연결되는 액션을 정의
    action.move_to_element(first_tag).move_to_element(second_tag).click().perform()

    # 잠깐 깜빡거리는 UI에서 원하는 행동을 할 때 까지 기다려달라는 메소드
    seoul_tag = WebDriverWait(driver, 10).until(
        # 해당 element가 클릭할 수 있게 되면 클릭 해달라는 말(시간을 기다리지 않을 수도 있음)
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a")
        )
    )
    seoul_tag.click()

    # 전체 라고 적어져 있는 요소의 클래스 네임으로 버튼 찾기
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((
        By.CLASS_NAME, 'set_gugun_cd_btn')))
    gu_elements = driver.find_elements(By.CLASS_NAME, 'set_gugun_cd_btn')
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#mCSB_2_container > ul > li:nth-child(1) > a")
        )
    )
    gu_elements[0].click()
    # 5초 기다리기 
    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located(
        (By.CLASS_NAME, 'quickResultLstCon')))

    req = driver.page_source
    # 2번자 파라미터에 파서에 대해 적어줘야한다.
    soup = BeautifulSoup(req, 'html.parser')
    # ul 태그명에서 li를 모두 찾아서 stores에 배열로? 저장
    stores = soup.find('ul', 'quickSearchResultBoxSidoGugun').find_all('li')

    # 데이터들을 저장할 리스트
    store_list = []
    addr_list =[]
    lat_list = []
    lng_list = []

    for store in stores:
        # strong 태그 text에 있는 지점명을 찾아온다.
        store_name = store.find('strong').text
        # p 태그안에 주소와 전화번호가 같이 있다.
        store_addr = store.find('p').text
        # 3번째 파라미터에 들어간 문자열에서 정규표현식에 맞는지 확인해서
        # 2번째 파라미터로 변환, strip() 으로 앞뒤 공백도 제거
        store_addr = re.sub(r'\d{4}-\d{4}$','',store_addr).strip()
        # 데이터 속성에 있던 위,경도를 가져온다.
        store_lat = store['data-lat']
        store_lng = store['data-long']

        # list 에 데이터 추가
        store_list.append(store_name)
        addr_list.append(store_addr)
        lat_list.append(store_lat)
        lng_list.append(store_lng)

    # 데이터 프레임으로 만들기
    df = pd.DataFrame({
        'store' : store_list,
        'addr' : addr_list,
        'lat' : lat_list,
        'lng': lng_list
    })

    time.sleep(3)
    driver.quit()
    return df

# csv 파일로 저장하기
starbucks_df = fetch_starbucks()
starbucks_df.to_csv('starbucks_seoul.csv', index=False, encoding="utf-8-sig")
print("데이터가 starbucks_seoul.csv 파일로 저장되었습니다.")