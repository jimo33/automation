from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import misc
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
#whoop

assert "No results found." not in driver.page_source
driver.back()

# driver.close()


# from selenium.webdriver.common.devtools.v105.dom().selenium

# from import.selenium.webdriver
# import misc

# PATH = "C:\Automation\driver\chromedriver.exe"

# driver = webdriver.Chrome(PATH)
# driver.find_element(by.ID)
# driver.manage().window().maximize()
# driver.tools

# print(driver.title)
# driver.quit()