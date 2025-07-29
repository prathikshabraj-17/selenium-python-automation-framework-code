import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#from webdriver_manager.microsoft import EdgeChromiumDriverManager
#driver = webdriver.Edge(EdgeChromiumDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://axontest.eoxvantage.com/apps/StorageTankLiability/form/quote")
driver.maximize_window()
time.sleep(10)

