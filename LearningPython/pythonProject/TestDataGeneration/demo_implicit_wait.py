import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

executable_path=ChromeDriverManager().install
driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


class DemoImplicitWait():
  def demo_imp_wait(self):

       # 1. LOGIN
       driver.get("https://apptest.eoxvantage.com/")
       driver.maximize_window()
       driver.find_element(By.ID, "username").send_keys("prathikshar")
       driver.find_element(By.ID, "password").send_keys("Welcome321!")
       driver.implicitly_wait(10)
       driver.find_element(By.XPATH, "//button[@type='submit']").click()
       time.sleep(10)

       # 2. Wait for the Menu image to be clickable and click
       driver.find_element(By.XPATH, "//img[@alt='Menu']").click()
       driver.implicitly_wait(10)
       driver.find_element(By.XPATH, "//div[@class='appcaption'][normalize-space()='Helpdesk']").click()

       # 3. Navigate to Helpdesk
       driver.find_element(By.CSS_SELECTOR, "a[title='New Ticket']").click()

       #4.  Select Department
       driver.find_element(By.XPATH, "//div[@id='eupanup']//div[@class='form-control ui fluid selection dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--eupanup-category-item-choice-4']").click()


       #5. Choose Type
       driver.find_element(By.XPATH,"//div[@class='choices__item choices__placeholder choices__item--selectable']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--eb3j6yr-issue_type_it-item-choice-1']").click()
       driver.implicitly_wait(8)

       #6.Choose Production Support Category
       driver.find_element(By.XPATH, "//div[@id='e6wbe2o']//div[@class='form-control ui fluid selection dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--e6wbe2o-category_PS-item-choice-1']").click()

       #7. Enter value to the Subject text field
       driver.find_element(By.XPATH, "//input[@id='eoixwc-name']").send_keys("Test data")

       #8. Enter value to the Description text field
       driver.find_element(By.XPATH, "//div[@aria-label='Rich Text Editor, main']").send_keys("Test Test Test")

       #9.Select Observer
       driver.find_element(By.XPATH, "//input[@placeholder='Select observers']").click()
       driver.find_element(By.XPATH, "//input[@placeholder='Select observers']").send_keys("Sound")
       driver.find_element(By.XPATH,"//div[@id='choices--ez1ndx-observers-item-choice-2']").click()

       #10. Select Severity
       driver.find_element(By.XPATH, "//div[@id='ehekim']//div[@class='form-control ui fluid selection dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--ehekim-severity-item-choice-1']").click()

       #11. Select Priority
       driver.find_element(By.XPATH, "//div[@id='elgdqvt']//div[@role='combobox']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--elgdqvt-priority-item-choice-2']").click()

       #12.File upload
       driver.find_element(By.XPATH,"//div[@class='fileSelector']").click()
       driver.find_element(By.XPATH,"//a[@class='browse']").click()


       #CLICK ON SUBMIT
       driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()


impwait = DemoImplicitWait()
impwait.demo_imp_wait()

