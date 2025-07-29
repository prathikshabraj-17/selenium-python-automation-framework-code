import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoGetAttributeValue():
    def demo_getvalue(self):

        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        attr_value = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("id")
        print(attr_value)
        time.sleep(6)

attrobj = DemoGetAttributeValue()
attrobj.demo_getvalue()









