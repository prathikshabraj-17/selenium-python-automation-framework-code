import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoGetText():
    def demo_gettext(self):

        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        text = driver.find_element(By.XPATH, "//p[contains(text(),'On Yatra.com, you can tailor your trip from end-to')]").text
        text1 = driver.find_element(By.LINK_TEXT, "Yatra for Business").text
        print(text,text1)

        time.sleep(60)


findbyid = DemoGetText()
findbyid.demo_gettext()







