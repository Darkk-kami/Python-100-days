from selenium import webdriver
from selenium.webdriver.common import by, keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver(webdriver.Chrome):
    def __init__(self):
        self.driver_path = r"C:\tools\chromedriver-win64\chromedriver.exe"
        self.service = Service(self.driver_path)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.by = by.By
        self.keys = keys.Keys
        self.wait = WebDriverWait
        self.EC = EC
        super().__init__(service=self.service, options=self.chrome_options)

