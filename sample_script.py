from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# # create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# wait up to amount of sec
# work for all find_element() and find_elements()
# checks every 100ms for element presence
# put in the code once
driver.implicitly_wait(4)
driver.wait = WebDriverWait(driver, 15)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

# wait for 4 sec
sleep(4) # only stop for number of seconds

# click search button
# defined in the code, where we use
# checks for EC every 500ms
# fails with TimeoutException
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable' )
driver.find_element(By.NAME, 'btnK').click()
# driver.implicitly_wait(0) #if you dont want to wait

# verify search results
# assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
# verify search results yukaridakiyle ayni seyi yapiyor
driver.wait.until(EC.url_contains('Car'), message='word Car is not url')
driver.quit()
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from webdriver_manager.chrome import ChromeDriverManager

# # from time import sleep
#
# # get the path to the ChromeDriver executable
# # 	@@ -12,6 +14,15 @@
# # # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
#
# # wait up to N amount of sec
# # work for all find_element() and find_elements()
# # checks every 100 ms for element presence
# # put in the code once
# # if fails, we see NoSuchElementException
# driver.implicitly_wait(6)
#
# # driver.wait = WebDriverWait(driver, 10)
#
# # open the url
# driver.get('https://www.google.com/')
#
# 	# @@ -21,13 +32,17 @@
# search.send_keys('Car')
#
# # wait for 4 sec
# # sleep(7)  # stop for number of seconds
#
# # defined in the code, where we use
# # checks for EC every 500ms
# # fails with TimeoutException
# driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable')
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify search results
# # assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# # print('Test Passed')
# driver.wait.until(EC.url_contains('Car'), message='Word Car not in URL')
#
# driver.quit()