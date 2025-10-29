import pytest
import unittest
import time
from pages.spicejet_launch_page import LaunchPage
from pages.search_flights_results_page import SearchFlightResults
from selenium.webdriver.common.by import By
from testcases.conftest import setup
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack

@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlights(unittest.TestCase):
    # driver = None

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.lp = LaunchPage(self.driver)
        self.log = Utils.cust_logger()

    # @data(("Del", "Bengaluru", "26/10/2025"), ("Kol", "Bengaluru", "02/11/2025"))
    # @unpack
    @file_data("../testdata/testdata.json")
    # @file_data("../testdata/testyml.yaml")
    # @data(*Utils.read_data_from_excel("C:\\Users\\User\\PythonProject\\TestFrameworkDemo\\testdata\\testdataexcel.xlsx", "Sheet"))
    # @data(*Utils.read_data_from_csv("C:\\Users\\User\\PythonProject\\TestFrameworkDemo\\testdata\\testdatacsv.csv"))
    @unpack
    def test_search_and_verify_test1(self, departfrom, goingto, departuredate):
        search_flight_result = self.lp.search_Flights(departfrom, goingto, departuredate)
        self.lp.scroll_up_down(step=500, delay=2)
        self.lp.scroll_up_down(step=500, delay=2)
        sf = SearchFlightResults(self.driver)
        stop_filters = sf.get_search_flight_results()
        ut = Utils(self.driver)
        ut.assertListItemText(stop_filters, "Direct")



















        # for stop in stop_filters:
        #     if  "Direct" in stop.text:
        #         stop.click()
        #         self.driver.execute_script("arguments[0].click();", stop)
        #         self.driver.execute_script("arguments[0].scrollIntoView(true);", stop)
        #
        #         time.sleep(1)

    #
    #
    # def test_search_and_verify_kolkata(self):
    #     search_flight_result = self.lp.search_Flights("Kol", "Bengaluru", "01/11/2025")
    #     self.lp.scroll_up_down(step=300, delay=2)
    #     self.lp.scroll_up_down(step=500, delay=2)
    #     sf = SearchFlightResults(self.driver)
    #     stop_filters = sf.get_search_flight_results()
    #     ut = Utils(self.driver)
    #     ut.assertListItemText(stop_filters, "Direct")
    #     # Loop through and click 'Direct'
        # for stop in stop_filters:
        #     if "Direct" in stop.text:
        #         stop.click()
        #         self.driver.execute_script("arguments[0].click();", stop)
        #         self.driver.execute_script("arguments[0].scrollIntoView(true);", stop)
        #         time.sleep(1)