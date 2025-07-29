import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path=ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoSliders():
    def sliders_demo(self):
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)
        driver.get("https://www.snapdeal.com/products/mobiles-featured-phones?sort=plrty")
        driver.maximize_window()
        elem1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        elem2 = driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")
        actions = ActionChains(driver)
        actions.drag_and_drop_by_offset(elem1, 40, 0 ).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(elem2, -70, 0).perform()
        # actions.click_and_hold(elem1).pause(1).move_by_offset(50,0).release().perform()
        # actions.move_to_element(elem1).pause(1).click_and_hold(elem1).move_by_offset(80,0).release().perform()

        time.sleep(2)

ds = DemoSliders()
ds.sliders_demo()

