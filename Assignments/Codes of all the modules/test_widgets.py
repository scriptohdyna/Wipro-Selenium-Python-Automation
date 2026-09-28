import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")

    yield driver

    driver.quit()


# 1. Radio Buttons - execute first
@pytest.mark.order(1)
def test_radio_buttons(driver):
    wait = WebDriverWait(driver, 10)

    male = wait.until(
        EC.element_to_be_clickable((By.ID, "male"))
    )
    female = driver.find_element(By.ID, "female")

    male.click()
    assert male.is_selected()
    assert not female.is_selected()
    print("Radio button: Male selected")

    female.click()
    assert female.is_selected()
    assert not male.is_selected()
    print("Radio button: Female selected")


# 2. CheckBoxes - execute second
@pytest.mark.order(2)
def test_checkboxes(driver):
    wait = WebDriverWait(driver, 10)

    sunday = wait.until(
        EC.element_to_be_clickable((By.ID, "sunday"))
    )
    monday = driver.find_element(By.ID, "monday")

    sunday.click()
    monday.click()

    assert sunday.is_selected()
    assert monday.is_selected()
    print("Checkboxes: Sunday and Monday selected")

    sunday.click()
    assert not sunday.is_selected()
    print("Checkbox: Sunday deselected")


# 3. Drag and Drop - execute last
@pytest.mark.last
def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)

    source = wait.until(
        EC.visibility_of_element_located((By.ID, "draggable"))
    )
    target = wait.until(
        EC.visibility_of_element_located((By.ID, "droppable"))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        source
    )

    time.sleep(1)

    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()

    wait.until(
        lambda d: "Dropped" in target.text
    )

    assert "Dropped" in target.text
    print("Drag and Drop: Successful")