from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_selectors import home_page

import time

PATH = "C:\Automation\driver\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(home_page.url)
driver.maximize_window()

assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)


time.sleep(6)

assert "No results found." not in driver.page_source
print(driver.current_url)
print(driver.application_cache)
print(driver.current_window_handle)
print(driver.capabilities)
print(driver.file_detector)
# print(driver.page_source.title())
print(driver.title)
driver.quit()