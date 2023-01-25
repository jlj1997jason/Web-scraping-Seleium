from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.opentix.life/login')

# cookie Agreement
driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[2]/button").click()

# 帳號密碼的登入
account = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/label/input")
account.clear()
account.send_keys("0977350526")
password = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/div[2]/div[4]/form/div/label/input")
password.clear()
password.send_keys("qswses13579")
driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/div[2]/a").click()

cookies = driver.get_cookies()
for c in cookies:
    print(c)
    driver.add_cookie(c)

time.sleep(2)
# 搶票網址
# driver.get('https://www.opentix.life/cart/1593200866560258050/1593240306191699969')

driver.get('https://www.opentix.life/cart/1539089895752417283/1541369673743118337')
time.sleep(4)

# //*[@id="1樓1號門-2-19"]//*[@id="1樓1號門-2-17"]//*[@id="1樓2號門-2-16"]//*[@id="1樓2號門-2-18"]//*[@id="1樓1號門-2-23"]//*[@id="1樓1號門-2-21"]
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-2-23"]').click()
print("選擇座位!")


# 票價/html/body/div/div/div/div/div[1]/div[4]/div[2]/div/div/div[2]/div/ol/div/div[1]
driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div[1]/div[4]/div[2]/div/div/div[2]/div/ol/div/div[2]/div[1]").click()
print("選擇票價！")


driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-2-21"]').click()
print("選擇座位!")
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-2-19"]').click()
print("選擇座位!")
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-2-17"]').click()
print("選擇座位!")
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-2-16"]').click()
print("選擇座位!")
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-2-18"]').click()
print("選擇座位!")
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-2-22"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-2-20"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/section[2]/div/section/div/div[2]/a[2]").click()
print("加入購物車！")
