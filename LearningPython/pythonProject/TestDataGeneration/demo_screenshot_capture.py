import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from webdriver_manager.chrome import ChromeDriverManager
# driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())


executable_path = ChromeDriverManager().install
driver: WebDriver = webdriver.Chrome()

class DemoScreenshot():
   def demo_screen_capture(self):
       driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
       driver.maximize_window()

       continuedemo = driver.find_element(By.XPATH, "//button[@id = 'login-continue-btn']")
       continuedemo.screenshot(".\\test.png")
       continuedemo.click()
       time.sleep(2)
       driver.get_screenshot_as_file("C:\\python selenium\\prathi.png")
       driver.save_screenshot(".\\test3.png")

ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screen_capture()