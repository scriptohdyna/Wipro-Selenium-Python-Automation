from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername = "chrome"

if browsername.lower() == "chrome":
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

else:
    raise Exception(
        "Invalid browser name. Please choose 'chrome' or 'firefox'."
    )

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()

driver.find_element(
    By.XPATH, "//input[@id='email']"
).send_keys("test@example.com")

time.sleep(2)

driver.quit()