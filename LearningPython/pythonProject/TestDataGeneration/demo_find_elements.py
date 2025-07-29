import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path=ChromeDriverManager().install
driver = webdriver.Chrome()
class DemoFindElementByIDandName():
    def locate_by_id_demo(self):
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install)
        driver.get(" https://www.yatra.com/")
        driver.maximize_window()
        lista = driver.find_elements(By.TAG_NAME, "body")
        print(len(lista))
        for i in lista:
            print(i.text)


        time.sleep(60)


findbyid = DemoFindElementByIDandName()
findbyid.locate_by_id_demo()







