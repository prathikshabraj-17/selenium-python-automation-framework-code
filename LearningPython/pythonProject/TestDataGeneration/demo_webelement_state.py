import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoElementState():
    def demo_enable_disable(self):
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo_state)

        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("prathiksha")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("prathikshar")
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_displayed()
        print(demo_state1)
        driver.maximize_window()

        time.sleep(4)


demostate = DemoElementState()
demostate.demo_enable_disable()







