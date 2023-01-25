from selenium import webdriver
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import time

sched = BlockingScheduler(timezone='Asia/Taipei')
driver = webdriver.Chrome('./chromedriver')
account = ""
password = ""

driver.get('https://www.opentix.life/login')

# cookie Agreement
driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div[2]/button").click()

# 帳號密碼的登入
account = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/label/input")
account.clear()
account.send_keys(account)
password = driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/div[2]/div[4]/form/div/label/input")
password.clear()
password.send_keys(password)
driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/div[2]/a").click()


cookies = driver.get_cookies()
for c in cookies:
    print(c)
    driver.add_cookie(c)

time.sleep(2)


# def job():
# 搶票網址
driver.get(
    'https://www.opentix.life/cart/1593200866560258050/1593240306191699969')

# driver.get('https://www.opentix.life/cart/1539089895752417283/1541369673743118337')
time.sleep(4)

# //*[@id="1樓1號門-1-1"] //*[@id="1樓2號門-1-2"]
driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-1"]').click()
print("選擇座位!")

# 票價//*[@id="container"]/div[4]/div[2]/div/div/div[2]/div/ol/div/div[2]/div[1]
# //*[@id="container"]/div[4]/div[2]/div/div/div[2]/div/ol/div/div
driver.find_element_by_xpath(
    "/html/body/div/div/div/div/div[1]/div[4]/div[2]/div/div/div[2]/div/ol/div/div[2]/div[1]").click()
print("選擇票價！")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-23"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-21"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-21"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-19"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-17"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-15"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-13"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-11"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-9"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-7"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-5"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓1號門-1-3"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-2"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-4"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-6"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-8"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-10"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-12"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-14"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-16"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-18"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-20"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    '//*[name()="svg" and @id="canvas"]//*[name()="svg" and @id="exportSVG"]//*[name()="text" and @id="1樓2號門-1-22"]').click()
print("選擇座位!")

driver.find_element_by_xpath(
    "/html/body/div[1]/div/div/div/div[1]/section[2]/div/section/div/div[2]/a[2]").click()
print("加入購物車！")


# 在2022年12月3日執行
# sched.add_job(job, 'date', run_date=datetime(
#     2022, 12, 3, 12, 0, 1))

# sched.start()
