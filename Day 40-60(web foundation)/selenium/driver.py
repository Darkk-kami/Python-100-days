from selenium import webdriver
from selenium.webdriver.common import by, keys
from selenium.webdriver.chrome.service import Service


class Driver(webdriver.Chrome):
    def __init__(self):
        self.driver_path = r"C:\tools\chromedriver-win64\chromedriver.exe"
        self.service = Service(self.driver_path)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.by = by.By
        self.keys = keys.Keys
        super().__init__(service=self.service, options=self.chrome_options)

