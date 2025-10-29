from time import sleep

from pages.search_flights_results_page import SearchFlightResults
from selenium.webdriver.common.keys import Keys
from base.base_driver import BaseDriver
from selenium.webdriver.common.by import By
from utilities.utils import Utils


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = Utils.cust_logger()

    # ---- Locators ----
    DEPART_FROM_FIELD = "//div[@data-testid='to-testID-origin']//input[@type='text']"
    GOING_TO_FIELD = "//div[@data-testid='to-testID-destination']//input[@type='text']"
    SELECT_DATE_FIELD = "//*[@data-testid='departure-date-dropdown-label-test-id']"
    SEARCH_BUTTON = "//div[@data-testid='home-page-flight-cta']"   # shorter locator
    DIRECT_FLIGHT = "//*[normalize-space(text())='All Flights'] | //*[normalize-space(text())='Direct']"
    # ---- Getters ----
    def get_depart_from_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def get_going_to_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def get_select_date_field(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def get_search_button(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)

    # def get_direct_flights(self):
    #      return self.wait_until_element_is_clickable(By.XPATH, self.DIRECT_FLIGHT)

    # ---- Actions ----
    def enter_depart_from_location(self, departlocation):
        self.logger.info(f"Entering 'Depart From' location: {departlocation}")
        depart_from = self.get_depart_from_field()
        depart_from.click()
        depart_from.clear()
        depart_from.send_keys(departlocation[:3])
        # sleep(2)
        depart_from.send_keys(Keys.ENTER)
        options = self.wait_for_presence_of_all_elements(
            By.XPATH, "//div[@class='css-76zvg2 r-homxoj r-ubezar']"
        )

        for opt in options:
            if departlocation in opt.text:
                opt.click()
                break

    def enter_going_to_location(self, geolocation):
        self.logger.info(f"Entering 'Going to' location: {geolocation}")
        going_to = self.get_going_to_field()
        going_to.click()
        going_to.send_keys(geolocation[:3])
        # sleep(2)
        going_to.send_keys(Keys.ENTER)
        options = self.wait_for_presence_of_all_elements(
            By.XPATH, "//div[@class='css-76zvg2 r-cqee49 r-ubezar r-1kfrs79']"
        )

        for opt in options:
            if geolocation in opt.text:
                opt.click()
                break

        # assert "Bengaluru" in going_to.get_attribute("value")

    def depart_date(self, departdate):
        # Click date field
        self.logger.info(f"Entering 'Departure Date' Date: {departdate}")

        departure_date = self.wait_until_element_is_clickable(
            By.XPATH, self.SELECT_DATE_FIELD
        )

        # Split date
        day, month, year = departdate.split("/")
        month_name = {
            "01": "January", "02": "February", "03": "March", "04": "April",
            "05": "May", "06": "June", "07": "July", "08": "August",
            "09": "September", "10": "October", "11": "November", "12": "December"
        }[month]

        # Pick date
        calendar = self.wait_for_presence_of_element(
            By.XPATH, f"//div[@data-testid='undefined-month-{month_name}-{year}']"
        )
        date_elem = calendar.find_element(
            By.XPATH, f".//div[@data-testid='undefined-calendar-day-{int(day)}']"
        )
        date_elem.click()

    def click_search(self):
        self.get_search_button().click()
        sleep(5)

    # def click_direct_flights(self):
    #      self.get_direct_flights()

    def search_Flights(self, departlocation, geolocation, departdate):
        self.enter_depart_from_location(departlocation)
        self.enter_going_to_location(geolocation)
        self.depart_date(departdate)
        self.click_search()
        # self.click_direct_flights()
        search_flight_result = SearchFlightResults(self.driver)
        return search_flight_result




























 # # def goingto(self, goingto):
 #    #     going_to = self.wait_until_element_is_clickable(
 #    #         By.XPATH, "//div[@data-testid='to-testID-destination']//input[@type='text']"
 #    #     )
 #    #     going_to.click()
 #    #     going_to.send_keys(goingto[:3])
 #    #
 #    #     options = self.wait_for_presence_of_all_elements(
 #    #         By.XPATH, "//div[@class='css-76zvg2 r-cqee49 r-ubezar r-1kfrs79']"
 #    #     )
 #    #     for opt in options:
 #    #         if "Bengaluru" in opt.text:
 #    #             opt.click()
 #    #             break
 #
 #    # ---- DATE ----
 #    def departdate(self, departdate):
 #        departure_date = self.wait_until_element_is_clickable(
 #            By.XPATH, "//*[@data-testid='departure-date-dropdown-label-test-id']")
 #        self.driver.execute_script("arguments[0].click();", departure_date)
 #        day, month, year = departdate.split("/")
 #
 #        month_name = {
 #            "01": "January", "02": "February", "03": "March", "04": "April",
 #            "05": "May", "06": "June", "07": "July", "08": "August",
 #            "09": "September", "10": "October", "11": "November", "12": "December"
 #        }[month]
 #
 #        calendar = self.wait_for_presence_of_element(
 #            By.XPATH, f"//div[@data-testid='undefined-month-{month_name}-{year}']"
 #        )
 #        date_elem = calendar.find_element(
 #            By.XPATH, f".//div[@data-testid='undefined-calendar-day-{int(day)}']"
 #        )
 #        date_elem.click()
 #
 #    # ---- SEARCH ----
 #    def clicksearch(self):
 #        self.driver.find_element(
 #            By.XPATH,
 #            "//div[@class='css-1dbjc4n r-1awozwy r-z2wwpe r-1loqt21 "
 #            "r-18u37iz r-1777fci r-d9fdf6 r-1w50u8q r-ah5dr5 r-1otgn73']"
 #        ).click()
 #        sleep(8)
 #
 #    def getDepartFromField(self):
 #        pass
 #

