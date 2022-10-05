from selenium import webdriver
# from selenium.webdriver.common.devtools.v105.dom().selenium

# from import.selenium.webdriver
import misc

PATH = "C:\Automation\driver\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get(misc.url)
# driver.find_element(by.ID)
# driver.manage().window().maximize()


print(driver.title)
driver.quit()