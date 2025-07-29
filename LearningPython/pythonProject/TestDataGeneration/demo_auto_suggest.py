import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# driver: WebDriver = webdriver.Chrome(ChromeDriverManager().install())


executable_path = ChromeDriverManager().install
driver: WebDriver = webdriver.Chrome()


def demo_autosuggest_dropdown():
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
    depart_from.click()
    time.sleep(2)
    depart_from.send_keys("New York")
    time.sleep(2)
    depart_from.send_keys(Keys.ENTER)
    time.sleep(2)
    going_to = driver.find_element(By.XPATH, "//input[@id ='BE_flight_arrival_city']")
    time.sleep(2)
    going_to.send_keys("NEW")
    time.sleep(2)
    # going_to.send_keys(Keys.ENTER)
    # time.sleep(3)
    search_results = driver.find_elements(By.XPATH, "//body/div[@class='theme-snipe']/div[@id='themeSnipe']/section[@class='wrapper']/div[@class='vertical_search_engine']/div[@class='bookingEngineWrapper']/div[@class='smooth-banner-transition']/section[@class='yt-booking-engine-snipe']/div[@class='be-container-snipe']/div[@id='booking_engine_modues']/div[@type='flights']/div[@id='BE_flight_form_wrapper']/div[@class='journey-details clearfix']/div[@class='oneway-roundtrip CitySwap']/ul[@class='clearfix']/li/ul[@class='from-to dflex w94 clearfix safariFix focus-on-field focus-field-arrival-city']/li[@class='flex1 destAutoSugestField safariFix__field activeBox safariFix__field--fifty']/div/div[@class='ac_results dest_ac']/ul/div[@class='viewport']/div/div[1]")
    print(len(search_results))
    for results in search_results:
        if "New York (JFK)" in results.text:
            results.click()
            time.sleep(3)


class DemoAutosuggest():
    pass

dauto = DemoAutosuggest()
demo_autosuggest_dropdown()



