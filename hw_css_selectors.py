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

driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=GVSG9XMZB3BE1T2VSFA2&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# textbox 1
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
# textbox 2
driver.find_element(By.CSS_SELECTOR, '#ap_email')
# textbox 3
driver.find_element(By.CSS_SELECTOR, '#ap_password')
# textbox 4
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
# amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# Create account
driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']")
# Passwords must be at least 6 characters.
driver.find_element(By.XPATH,"//div[@class='a-box a-alert-inline a-alert-inline-info auth-inlined-information-message a-spacing-top-mini']//div[@class='a-alert-content']")
# Create your Amazon account
driver.find_element(By.ID, 'continue')
# Conditions of use
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[text()='Conditions of Use']")
# Privacy Notice
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[text()='Privacy Notice']")
# Sign in
driver.find_element(By.XPATH,"//a[@class='a-link-emphasis']")


sleep(5)
