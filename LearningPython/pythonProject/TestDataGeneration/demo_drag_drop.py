import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path=ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoDragDrop():
    def drag_drop(self):
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@class='demo-frame']"))
        time.sleep(2)
        elem1 = driver.find_element(By.XPATH, "//div[@id='draggable']")
        time.sleep(2)
        elem2 = driver.find_element(By.XPATH, "//div[@id='droppable']")
        time.sleep(2)
        actions = ActionChains(driver)
        actions.drag_and_drop(elem1, elem2).perform()
        # actions.drag_and_drop_by_offset(elem1, )
        time.sleep(2)

dd = DemoDragDrop()
dd.drag_drop()











