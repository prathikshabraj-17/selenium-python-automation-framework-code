import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoMouseOver():
    def demo_mouse_events(self):
        driver.get("https://www.yatra.com/flights")
        driver.maximize_window()
        time.sleep(2)
        morebuttons = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        myaccount_link = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        achains = ActionChains(driver)
        achains.move_to_element(myaccount_link).perform()
        time.sleep(4)
        achains.move_to_element(morebuttons).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(2)


dmouse = DemoMouseOver()
dmouse.demo_mouse_events()
