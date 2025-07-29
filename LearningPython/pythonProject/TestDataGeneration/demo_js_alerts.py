import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path = ChromeDriverManager().install
driver = webdriver.Chrome()


class DemoJSPopup():
    def demo_js_alerts(self):
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")
        #accept alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
        #dismiss alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        #send text in alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.send_keys("Prathiksha B Raj")
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

dpopup = DemoJSPopup()
dpopup.demo_js_alerts()
