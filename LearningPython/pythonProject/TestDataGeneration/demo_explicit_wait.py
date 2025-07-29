from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

executable_path=ChromeDriverManager().install
driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


class DemoExplicitWait():
  def demo_exp_wait(self):

       #  LOGIN
       driver.get("https://apptest.eoxvantage.com/")
       driver.maximize_window()
       driver.find_element(By.ID, "username").send_keys("prathikshar")
       driver.find_element(By.ID, "password").send_keys("Welcome321!")
       driver.find_element(By.XPATH, "//button[@type='submit']").click()
       driver.explicit_wait(20)

       #  Wait for the Menu image to be clickable and click
       driver.find_element(By.XPATH, "//img[@title='Applications']").click() # eox Menu
       driver.implicitly_wait(8)
       driver.find_element(By.XPATH,"//div[@class='appcaption'][normalize-space()='Quality Management']").click()

       # Navigate to QMS new ticket
       driver.find_element(By.XPATH, "//a[@title='New Policy']").click()
       driver.implicitly_wait(8)

       # Enter value to the Title field
       driver.find_element(By.XPATH, "//input[@id='e13uj3i-name']").send_keys("Test Eox policy")
       driver.implicitly_wait(8)

       # Enter value to the Document number
       driver.find_element(By.XPATH, "//input[@id='eju8399-documentNumber']").send_keys("11222024")

      # Select status from the dropdown
       driver.find_element(By.XPATH, "//div[@id='e18fazk']//div[@class='choices__list choices__list--dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--e18fazk-status-item-choice-2']").click()

      # Select category
       driver.find_element(By.XPATH, "//div[@id='ejh12dh']//div[@class='form-control ui fluid selection dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='ejh12dh']//div[@role='listbox']").click()

      #Select Client
       driver.find_element(By.XPATH, "//div[@id='ezo0lh']//div[@class='form-control ui fluid selection dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='ezo0lh']//input[@placeholder='Type to search']").send_keys("hu")
       driver.find_element(By.XPATH, "//div[@id='choices--ezo0lh-client-item-choice-42']").click()

      #Select Parent
       driver.find_element(By.XPATH, "//div[@id='e7utarr']//div[@class='form-control ui fluid selection dropdown']").click()
       driver.find_element(By.XPATH, "//div[@id='choices--e7utarr-parent_task-item-choice-13']").click()




expwait = DemoExplicitWait()
expwait.demo_exp_wait()