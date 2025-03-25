from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

#AMAZON LOGO
driver.find_element(By.CSS_SELECTOR,'.a-icon a-icon-logo')
#CREATE ACCOUNT HEADING
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
#YOUR NAME TEXTBOX
driver.find_element(By.ID, 'ap_customer_name')
#email field
driver.find_element(By.ID, 'ap_email')
#password field
driver.find_element(By.ID, 'ap_password')
#Password alert
driver.find_element(By.ID, 'ap_password_context_message_section')
#re-enter password field
driver.find_element(By.ID, 'ap_password_check')
#continue button
driver.find_element(By.ID, 'continue')
#condition of use
driver.find_element(By.CSS_SELECTOR,"[href*='condition_of_use']")
#condition of use
driver.find_element(By.CSS_SELECTOR,"[href*='condition_of_use']")
#Privacy Notice
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_privacy_notice']")
#Sign in
driver.find_element(By.CSS_SELECTOR,'h1.a-link-emphasis')