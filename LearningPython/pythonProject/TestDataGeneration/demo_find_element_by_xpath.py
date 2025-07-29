import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path=ChromeDriverManager().install
driver = webdriver.Chrome()
class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.find_element_by_id('login-form').send_keys('prathikshar@eox.com')
        element = driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("prathiksha@eox.com")
        # driver.find_element_by_xpath("//input[@id='login-input']").send_keys('prathikshar@eox.com')
        time.sleep(160)

findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()






