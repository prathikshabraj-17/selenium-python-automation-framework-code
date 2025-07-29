import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoMultipleWindows():
    def demo_windows(self):
        driver.get("https://testingsite-35971.web.app/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Open New Tab / Window']").click()

        driver.get("https://testingsite-35971.web.app/newwindowwithtabs")
        time.sleep(6)




dmultiplewindows = DemoMultipleWindows()
dmultiplewindows.demo_windows()






