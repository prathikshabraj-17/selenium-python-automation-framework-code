import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoDropdownSingleSelect():
    def demo_dropdown(self):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        dropdown = driver.find_element(By.NAME, "dropdown-class-example")
        dd = Select(dropdown)

        dd.select_by_index(1)
        time.sleep(3)

        dd.select_by_visible_text("Option2")
        time.sleep(3)

        dd.select_by_value("option3")
        time.sleep(3)


dddemo = DemoDropdownSingleSelect()
dddemo.demo_dropdown()







