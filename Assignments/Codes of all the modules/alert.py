from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Click the Alert button
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert

print(alert.text)

alert.accept()

time.sleep(2)
driver.quit()