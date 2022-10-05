from selenium import webdriver

import misc

PATH = "C:\Automation\driver\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(misc.url)

# driver.manage().window().maximize()


print(driver.title)
driver.quit()