import time
import logging
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from utilities.utils import Utils  # adjust import path if needed

class SearchFlightResults(BaseDriver):
    log = Utils.cust_logger(logLevel=logging.WARNING)
    # log.info("Logger initialized successfully in SearchFlightResults page")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SEARCH_FLIGHT_RESULTS = "//*[normalize-space(text())='All Flights'] | //*[normalize-space(text())='Direct']"

    def get_search_flight_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flights_by_stop(self):
        results = self.wait_for_presence_of_all_elements((By.XPATH, "//div[@id='list-results-section-0']"))
        assert len(results) > 0



