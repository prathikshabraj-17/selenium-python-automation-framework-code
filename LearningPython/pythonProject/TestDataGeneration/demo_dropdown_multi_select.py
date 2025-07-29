import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoDropdownMultiSelect():
    def demo_dropdown(self):
        driver.get("https://testingsite-35971.web.app/")
        driver.maximize_window()
        dd_demo = driver.find_element(By.ID, "multiselect")

        dd_multi = Select(dd_demo)

        dd_multi.select_by_index(1)
        dd_multi.select_by_value("m1")
        dd_multi.select_by_visible_text("MultiSelect 5")
        dd_multi.select_by_index(3)
        dd_multi.select_by_value("m7")
        dd_multi.select_by_visible_text("MultiSelect 8")
        time.sleep(5)


demo_multiselect = DemoDropdownMultiSelect()
demo_multiselect.demo_dropdown()





