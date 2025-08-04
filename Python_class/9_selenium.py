# pip install selenium
# Selenium은 웹 애플리케이션을 자동화하기 위한 오픈 소스 툴로, 브라우저를 프로그래밍적으로 제어하여 사람처럼 웹을 탐색하거나 상호작용할 수 있게 합니다. 주로 웹 테스트 자동화와 크롤링에 사용되며, 동적인 콘텐츠나 자바스크립트 렌더링이 필요한 웹 페이지에서도 효과적으로 동작합니다.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 창이 떴다가 바로 내려감
driver = webdriver.Chrome()
# google로 이동 되었다가 내려감
driver.get('https://www.google.com')
# html 요소중에 파라미터에 적은 요소를 찾는다
search = driver.find_element('name', 'q')
# 찾은 search 에 '날씨' 라는 text를 적는다.
search.send_keys('날씨')
# 검색실행
search.send_keys(Keys.RETURN)

# 10초 대기하기
time.sleep(10)