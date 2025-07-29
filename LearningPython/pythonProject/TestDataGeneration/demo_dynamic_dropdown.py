import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoDynamicDropdown():
    def demo_dynamic_dropdown(self):
        driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@placeholder='Type to Select']").click()
        driver.find_element(By.XPATH,"//input[@placeholder='Type to Select']").send_keys("Ind")
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[text()='India']").click()
        time.sleep(2)


ddynamicdropdown = DemoDynamicDropdown()
ddynamicdropdown.demo_dynamic_dropdown()








