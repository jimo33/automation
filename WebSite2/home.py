from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_selectors2 import home_page
from page_selectors2 import location_url
import time
import logging

PATH = "C:\Automation\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(location_url.motionindstries)

# solutions = driver.find_element(By.XPATH, home_page.SolutionsUrl)
# print("Solutions link is displayed", solutions.is_displayed())
# solutions.is_displayed()
#
# platform = driver.find_element(By.XPATH, home_page.PlatformUrl)
# print("Platform link is displayed", platform.is_displayed())
# platform.is_displayed()
#
# resources = driver.find_element(By.XPATH, home_page.ResourcesUrl)
# print("Resources link is displayed", resources.is_displayed())
# resources.is_displayed()
#
# company = driver.find_element(By.XPATH, home_page.CompanyUrl)
# print("Company link is displayed", company.is_displayed())
# company.is_displayed()
#
# contact = driver.find_element(By.XPATH, home_page.ContactUrl)
# print("Contact link is displayed", contact.is_displayed())
# contact.is_displayed()
#
# tryit = driver.find_element(By.XPATH, home_page.TryItUrl)
# print("Try It link is displayed", tryit.is_displayed())
# tryit.is_displayed()
#
# signin = driver.find_element(By.XPATH, home_page.SignInUrl)
# print("Sign In link is displayed", signin.is_displayed())
# signin.is_displayed()
#
# pricing = driver.find_element(By.XPATH, home_page.pricingUrl)
# print("Pricing link is displayed", pricing.is_displayed())
# pricing.is_enabled()
# pricing.click()
#
# # time.sleep(3)
# brand = driver.find_element(By.XPATH, home_page.brandIconUrl)
# print("Brand link is displayed", brand.is_displayed())
# brand.click()

time.sleep(3)
# assert "Python" in driver.title

# elem = driver.find_element(By.NAME, (home_page.search))
# elem.clear()
# time.sleep(3)
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# time.sleep(3)
# assert "No results found." not in driver.page_source

print(driver.title)
driver.quit()