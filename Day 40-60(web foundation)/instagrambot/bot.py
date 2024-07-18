import time

from selenium.common import ElementClickInterceptedException

from driver import Driver


class InstagramFollowerBot:
    def __init__(self):
        self.driver = Driver()

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")

        user_name = self.driver.wait(self.driver, 10).until(
            self.driver.EC.presence_of_element_located((self.driver.by.NAME, "username")))

        user_name.send_keys(username)
        passwd = self.driver.find_element(self.driver.by.NAME, value="password")
        passwd.send_keys(password)
        login_button = self.driver.wait(self.driver, 10).until(
            self.driver.EC.element_to_be_clickable((self.driver.by.CSS_SELECTOR, "button[type='submit']")))

        login_button.click()

        time.sleep(40)

        not_now_button = self.driver.wait(self.driver, 10).until(
            self.driver.EC.element_to_be_clickable((self.driver.by.XPATH, "//div[text()='Not now']"))
        )
        not_now_button.click()
        time.sleep(4)
        not_now_button2 = self.driver.wait(self.driver, 10).until(
            self.driver.EC.element_to_be_clickable((self.driver.by.XPATH, "//button[text()='Not Now']"))
        )
        not_now_button2.click()

    def find_followers(self, name):
        search_icon = self.driver.find_element(self.driver.by.CSS_SELECTOR, "svg[aria-label='Search']")
        search_icon.click()
        search_input = self.driver.find_element(self.driver.by.CSS_SELECTOR, "input[aria-label='Search input']")
        search_input.send_keys(name)
        time.sleep(4)
        name_target = self.driver.find_element(self.driver.by.XPATH, f"//span[text()='{name}']")
        name_target.click()
        time.sleep(4)
        followers = self.driver.find_element(self.driver.by.CSS_SELECTOR, f"a[href='/{name}/followers/']")
        followers.click()

    def follow(self):
        follow_list = self.driver.find_element(self.driver.by.XPATH,
                                               value="/html/body/div[7]/div[2]/div/div/"
                                                     "div[1]/div/div[2]/div/div/div/div/"
                                                     "div[2]/div/div/div[3]/div[1]/div")

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow_list)

            follow_buttons = self.driver.find_elements(self.driver.by.CSS_SELECTOR, value='._aano button')

            for button in follow_buttons:
                try:
                    button.click()
                    time.sleep(2)

                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(self.driver.by.XPATH, value="//button[contains(text(), "
                                                                                         "'Cancel')]")
                    cancel_button.click()

