import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoRadio():
    def demo_radio_button(self):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        print(driver.find_element(By.XPATH,"(//input[@value='radio1'])[1]").is_selected())
        driver.find_element(By.XPATH,"(//input[@value='radio1'])[1]").click()
        time.sleep(3)
        print(driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]").is_selected())
        driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]").click()
        time.sleep(3)


radiodemo = DemoRadio()
radiodemo.demo_radio_button()
