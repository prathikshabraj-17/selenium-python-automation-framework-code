import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoRightDoubleClick():
    def demo_right_double(self, copyelem=None):
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(2)
        # # Right click
        # achains = ActionChains(driver)
        # elem1 = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # achains.context_click(elem1).perform()
        # time.sleep(2)
        #
        # if copyelem is not None:
        #    copyelem.click()
        #    time.sleep(2)

        # Double  click
        achains = ActionChains(driver)
        elem2 = driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(elem2).perform()
        time.sleep(2)



drightclick = DemoRightDoubleClick()
drightclick.demo_right_double()
