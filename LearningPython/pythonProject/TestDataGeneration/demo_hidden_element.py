import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoHiddenElements():
    def demo_is_displayed(self):
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem)
        elem1 = driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").is_displayed()
        print(elem1)
        driver.maximize_window()

        time.sleep(2)

    def demo_is_displayed_yathra(self):
        driver.get("https://www.yatra.com/hotels")
        driver.find_element(By.XPATH,"//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(4)
        elem = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(4)
        elem1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        print(elem1)

demoDisplayed = DemoHiddenElements()
# demoDisplayed.demo_is_displayed()
demoDisplayed.demo_is_displayed_yathra()





