from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

driver.maximize_window()

driver.get("https://text-compare.com/")

# Task 1 - Type text in the left text box
left_text = driver.find_element(By.CSS_SELECTOR, "textarea:nth-of-type(1)")
left_text.send_keys("Welcome to Selennium")

time.sleep(2)

# Task 2 - Copy whatever is there in the right panel to the left panel
act = ActionChains(driver)

right_text = driver.find_element(By.CSS_SELECTOR, "textarea:nth-of-type(2)")

act.click(right_text)

act.key_down(Keys.CONTROL)

act.send_keys("a")

act.key_up(Keys.CONTROL)

act.key_down(Keys.CONTROL)

act.send_keys("c")

act.key_up(Keys.CONTROL)

act.click(left_text)

act.key_down(Keys.CONTROL)

act.send_keys("v")

act.key_up(Keys.CONTROL)

act.perform()

time.sleep(3)

driver.quit()