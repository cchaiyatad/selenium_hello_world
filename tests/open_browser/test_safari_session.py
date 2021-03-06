import pytest

from selenium import webdriver

from selenium.webdriver.common.by import By

def test_safari_session():
    driver = webdriver.Safari()

    driver.get("https://google.com")

    assert driver.title == "Google"

    driver.implicitly_wait(0.5)

    search_box = driver.find_element(by=By.NAME, value="q")
    search_button = driver.find_element(by=By.NAME, value="btnK")

    search_box.send_keys("Selenium")
    search_button.click()

    search_box = driver.find_element(by=By.NAME, value="q")
    assert search_box.get_attribute("value") == "Selenium"

    driver.quit()


if __name__ == "__main__":
    test_safari_session()