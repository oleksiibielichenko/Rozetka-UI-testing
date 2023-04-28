import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService

service = ChromiumService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://www.rozetka.com.ua")

time.sleep(10)

driver.quit()
