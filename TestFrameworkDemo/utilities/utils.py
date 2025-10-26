import time
import inspect
import logging
import sys
import csv
# import openpyxl
# from openpyxl import load_workbook
# from pandas.io.sas.sas_constants import row_count_offset_multiplier


class Utils:
    def __init__(self, driver=None):
        self.driver = driver

    def assertListItemText(self, elements_list, value):
        for elem in elements_list:
            if elem.text.strip() == value:
                elem.click()
                time.sleep(1)
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
                time.sleep(1)

    @staticmethod
    def cust_logger(logLevel=logging.DEBUG):
        # Set class/method name from where it's called
        logger_name = inspect.stack()[1][3]

        # Create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)

        if not logger.handlers:
             # return logger

             fh = logging.FileHandler("automation.log", mode='a')
             fh.setLevel(logLevel)

             ch = logging.StreamHandler()
             ch.setLevel(logLevel)

             formatter = logging.Formatter(
                 '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                 datefmt='%d-%m-%Y %H:%M:%S'
             )

             fh.setFormatter(formatter)
             ch.setFormatter(formatter)

             logger.addHandler(fh)
             logger.addHandler(ch)

        return logger

    def read_data_from_excel(file_name, sheet):
        datalist = []
        wb = load_workbook(filename = file_name)
        sh = wb[sheet]

        row_ct = sh.max_row
        col_ct = sh.max_column

        for i in range(2, row_ct + 1):
            row = []
            for j in range(1, col_ct + 1):
                row.append(sh.cell(row=i, column=j).value)
            datalist.append(row)
        return datalist

    def read_data_from_csv(filename):
        #create an empty list
        datalist = []

        #open CSV File
        csvdata = open(filename, "r")

        #Create CSV reader
        reader = csv.reader(csvdata)
        #skip header
        next(reader)
        #add CSV rows to list
        for rows in reader:
            datalist.append(rows)
        return datalist