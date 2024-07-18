import time
from driver import Driver


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = Driver()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element(self.driver.by.CLASS_NAME, value="start-text")
        button.click()
        time.sleep(40)

        self.up = float(self.driver.find_element(self.driver.by.CLASS_NAME, "download-speed").text)
        self.down = float(self.driver.find_element(self.driver.by.CLASS_NAME, "upload-speed").text)
        self.driver.quit()

    def tweet_at_provider(self, username, passwd, up, down):
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(2)
        email = self.driver.find_element(self.driver.by.XPATH,
                                         value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/'
                                               'form/div/div[1]/label/div/div[2]/div/input')

        password = self.driver.find_element(self.driver.by.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/'
                                                  'form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(username)
        password.send_keys(passwd)
        time.sleep(2)
        password.send_keys(self.driver.keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(self.driver.by.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/'
                                                       'div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/'
                                                       'div[2]/div[1]/div/div/div/div/div/div/div/div/div/'
                                                       'div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when"
                 f" I pay for {down}down/{up}up?")

        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(self.driver.by.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                      'div/div/div/div[2]/div/div[2]/div[1]/div/div/div/'
                                                      'div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
