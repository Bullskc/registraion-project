from selenium import webdriver
from selenium.webdriver.edge import service
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.ie import service
import os

# 보호모드(인터넷옵션) 동일하게 작동
os.system('"c:/Users/SEC/Documents/protected_same.vbs"')

# IE 옵션 설정
ieOptions = webdriver.IeOptions()
ieOptions.add_additional_option("ie.edgechromium", True)
ieOptions.add_additional_option("ie.edgepath", 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')

# IEDriverServer 실행
driver = webdriver.Ie(executable_path='c:/Users/SEC/Desktop/PythonWorkspace/IEDriverServer.exe', options=ieOptions)

# 브라우저 창 최대화
driver.maximize_window()

# 원하는 페이지로 이동
driver.get('http://www.iros.go.kr/PMainJ.jsp')
driver.implicitly_wait(10)

# 4. 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id_user_id")
# id.clear()
id.click()
time.sleep(5)
id.send_keys("bullskc")


# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#password")
# pw.clear()
pw.click()
time.sleep(7)
pw.send_keys("26ej5082!")


# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#leftS > div:nth-child(2) > form > div.id_pw > ul > li.mt05 > a")
login_btn.click()

time.sleep(5)
main = driver.window_handles
for i in main:
    if i != main[0]:
        driver.switch_to.window(i)
        driver.close()

driver.switch_to.window(main[0])
driver.maximize_window()

time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="cenS"]/div/ul/li[2]/a').click()

time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="cenS"]/div/ul/li[2]/div/ul/li[5]/a').click()

time.sleep(3)
driver.find_element(By.XPATH,'//a[@title="작성완료된 신청서(출력가능)"]').click()


