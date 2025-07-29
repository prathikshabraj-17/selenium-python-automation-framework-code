import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class Demoseleniumlearning():
    def demo_broswer_methods(self):

        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(4)
        driver.back()
        driver.minimize_window()
        time.sleep(6)
        driver.quit()


demobrowser = Demoseleniumlearning()
demobrowser.demo_broswer_methods()







