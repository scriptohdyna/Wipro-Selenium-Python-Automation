from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys("John Doe")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[name='radioButton']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[id$='Option2']").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "input[id*='BoxOption']").click()
time.sleep(2)

driver.quit()