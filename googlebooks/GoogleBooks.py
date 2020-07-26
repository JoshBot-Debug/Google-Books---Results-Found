import requests
import re
from pandas import read_csv, DataFrame
import pathlib
from bs4 import BeautifulSoup
from selenium import webdriver
import os

class GoogleBooks:

    __Name = "GoogleBooks.py"
    __OutputFolder = os.getcwd()
    __csvName = ""
    
    def __init__(self):
        print(f'[{self.__Name}] : init')

        opts = webdriver.ChromeOptions()
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument("--headless") # This Does the Job without opening a chrome window
        opts.add_argument("--log-level=3")  # This does not log anything in the console
        self.__driver = webdriver.Chrome(options=opts) #If Chrome Fails, pass the executable path here  driver = webdriver.Chrome(options=opts,executable_path="path to driver (it should be in this directory)")


    def doSearch(self):
        self.__driver.get(self.create_url())
        html = self.__driver.find_element_by_id("result-stats").get_attribute('innerHTML')
        data = re.search('(.*)<nobr>',html).group(1)
        self.createCsv(data)


    def end(self):
        self.__driver.close()


    def createCsv(self, Data: str):
        self.__PathToCsv = self.__OutputFolder+"\\"+self.__csvName+".csv"
        data = [{"From Year":self.from_year,"To Year":self.to_year, "Number of Results":Data}]
        self.df = DataFrame(data)

        if pathlib.Path(self.__PathToCsv).exists():
            self.df.to_csv(self.__PathToCsv, mode='a',header=False, index=False) 
        else:
            self.df.to_csv(self.__PathToCsv, mode='w', index=False) 


    def setCavName(self, Name: str):
        self.__csvName = Name


    def create_url(self) -> str:
        self.__BaseUrl = f"https://www.google.com/search?q={self.search}&sxsrf=ALeKk00bQz6BmODCUgAiE1qrhBIUFdGa4A%3A1595753816449&source=lnt&tbs=cdr%3A1%2Ccd_min%3A{self.from_month}%2F{self.from_date}%2F{self.from_year}%2Ccd_max%3A{self.to_month}%2F{self.to_date}%2F{self.to_year}&tbm=bks"
        return self.__BaseUrl


    def setSearch(self, Search: str):
        self.search = Search

    def setFromDate(self, Date: str):
        self.from_date = Date
    
    def setFromMonth(self, Month: str):
        self.from_month = Month

    def setFromYear(self, Year: str):
        self.from_year = Year

    def setToDate(self, Date: str):
        self.to_date = Date
    
    def setToMonth(self, Month: str):
        self.to_month = Month

    def setToYear(self, Year: str):
        self.to_year = Year