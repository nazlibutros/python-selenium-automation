from selenium import webdriver
from selenium.webdriver.common.by import By #BU OLMASAYDI BY ID YI KULLANAMAZDIK
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# populate search field
# search by id
driver.find_element(By.ID,'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'searchDropdownBox')


# search by xpath
driver.find_element(By.XPATH,"//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH,"//input[@value='Go']")

# search by xpath multiple attribute
driver.find_element(By.XPATH,"//input[@class='nav-input nav-progressive-attribute' and @value='Go']")

# search bu xpath, text basina @ koymaya gerek yok
driver.find_element(By.XPATH,"//a[text()='Best Sellers' and class='nav-a']")
driver.find_element(By.XPATH,"//a[text()='Best Sellers' and @class='nav-a  ']")

# contains()
driver.find_element(By.XPATH,"//h2[text()='Scary-good Halloween costumes']")
driver.find_element(By.XPATH,"//h2[contains(text(), 'Scary-good')]")
driver.find_element(By.XPATH,"//h2[contains(aria-label(), 'Scary-good')]")

# parent to child
driver.find_element(By.XPATH,"//div[@id='nav-main']//a[text()='Best Sellers']")