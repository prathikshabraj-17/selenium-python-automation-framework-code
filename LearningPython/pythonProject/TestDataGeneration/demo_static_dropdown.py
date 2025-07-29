import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()

class DemoStaticDropdown:

    def demo_static_dropdown(self):
        driver.get("http://spicejet.com")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@data-testid='to-testID-origin']//input[@type='text']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[text()='Belagavi Airport']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[text()='Chennai International Airport']").click()
        time.sleep(3)

dstaticdropdown = DemoStaticDropdown()
dstaticdropdown.demo_static_dropdown()