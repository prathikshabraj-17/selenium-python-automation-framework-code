import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver: WebDriver = webdriver.Chrome()


class DemoIframe():
    def demo_frames(self):
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target")
        driver.maximize_window()
        time.sleep(3)
        #switch with iframe locator
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        #switch with index#
        driver.switch_to.frame("iframeResult")
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@id='getwebsitebtn']").click()

        time.sleep(3)

diframe = DemoIframe()
diframe.demo_frames()









