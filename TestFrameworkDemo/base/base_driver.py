import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseDriver:
    def __init__(self, driver, wait_time=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def scroll_up_down(self, step=300, delay=1):
        # scroll down
        self.driver.execute_script(f"window.scrollBy(0, {step});")
        time.sleep(delay)
        # scroll up
        self.driver.execute_script(f"window.scrollBy(0, -{step});")
        time.sleep(delay)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        list_of_elements = self.wait.until(
            EC.presence_of_all_elements_located((locator_type, locator))
        )
        assert len(list_of_elements) > 0, f"No elements found for locator: {locator}"
        return list_of_elements

    def wait_for_presence_of_element(self, locator_type, locator):
        element = self.wait.until(
            EC.presence_of_element_located((locator_type, locator))
        )
        return element

    def wait_until_element_is_clickable(self, locator_type, locator):
        element = self.wait.until(
            EC.element_to_be_clickable((locator_type, locator))
        )
        return element

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
