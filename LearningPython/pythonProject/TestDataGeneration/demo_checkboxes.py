import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoCheckboxes():
    def demo_checkboxes(self):
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@value='radio1']").click()
        time.sleep(3)
        var1 = driver.find_element(By.XPATH, "//input[@value='radio3']").is_selected()
        print(var1)
        driver.find_element(By.XPATH, "//input[@value='radio2']").click()
        time.sleep(6)

checkboxes = DemoCheckboxes()
checkboxes.demo_checkboxes()






