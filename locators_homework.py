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

driver.find_element(By.XPATH, "//a[@aria-label='www.amazon.com']") #Amazon logo
driver.find_element(By.ID, 'ap_email') #Email field
driver.find_element(By.ID, 'continue') #Continue button
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_condition_of_use')]") #Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]") #Privacy Notice link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']") #Need Help link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']") #Forgot your password link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']") #Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']") #Create your Amazon account button