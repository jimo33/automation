from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from page_selectors import home_page
from page_selectors import location_url
import time

PATH = "C:\Automation\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get(location_url.sauceLabs)

pricing = driver.find_element(By.XPATH, home_page.pricingUrl)
print("Pricing link is displayed", pricing.is_displayed())
pricing.is_enabled()
pricing.click()

# time.sleep(3)
brand = driver.find_element(By.XPATH, home_page.brandIcon)
print("Brand link is displayed", brand.is_displayed())
brand.click()

# time.sleep(3)
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