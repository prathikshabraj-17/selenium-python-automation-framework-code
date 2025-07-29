import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoJs():
    def demo_JavaScript(self, demo_element=None):
        driver.get("https://training.rcvacademy.com/")
        # driver.maximize_window()
        driver.execute_script("window.open('https://training.rcvacademy.com/')")
# if the url should open in the same line then use self command
        time.sleep(2)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();",demo_element)
        time.sleep(2)

demojs = DemoJs()
demojs.demo_JavaScript()