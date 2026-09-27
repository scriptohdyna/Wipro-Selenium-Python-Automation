from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/nested_frames")

outerframe = driver.find_element(By.XPATH, "//frame[@name='frame-top']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH, "//frame[@name='frame-middle']")
driver.switch_to.frame(innerframe)

textbox = driver.find_element(By.XPATH, "//body")
print(textbox.text)

time.sleep(2)

driver.quit()