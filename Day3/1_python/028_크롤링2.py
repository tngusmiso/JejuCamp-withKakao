from selenium import webdriver

path = "C:/crawling/chromedriver.exe"

#조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('https://www.google.com')

#페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
print('good')
print("Google" in driver.title)
print("Naver" in driver.title)
print('job')

#검색 입력 부분에 커서를 올리고
#검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
elem = driver.find_element_by_name("q")

#입력 부분에 default로 값이 있을 수 있어 비운다
elem.clear()

#검색어를 입력한다
elem.send_keys("Selenium")

#검색을 실행한다
elem.submit()

#검색이 제대로 됐는지 확인한다
assert "No results found." not in driver.page_source

#webdriver를 종료하여 창이 사라진다
driver.close()