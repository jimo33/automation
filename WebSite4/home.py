from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# import misc
PATH = "C:\Automation\driver\chromedriver.exe"

driver = webdriver.Chrome(PATH)
# driver.get("http://www.python.org")
driver.get(misc.url)
driver.maximize_window()

assert "Python" in driver.title

elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
