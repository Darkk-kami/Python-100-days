from driver import Driver
import os
import dotenv
import time


swipes = 0
dotenv.load_dotenv()

URL = ("https://tinder.com/")

driver = Driver()
driver.get(URL)

accept = driver.find_element(driver.by.XPATH, value='//*[@id="t41619109"]/div/div[2]/div/div/div[1]/'
                                                    'div[1]/button/div[2]/div[2]/div')
accept.click()
sign_in = driver.find_element(driver.by.LINK_TEXT, value="Log in")
sign_in.click()


sign_in_facebook = driver.wait(driver, 10).until(
    driver.EC.presence_of_element_located((driver.by.XPATH,
                                           '//*[@id="t-1686761967"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/'
                                           'span/div[2]/button/div[2]/div[2]/div[2]/div/div')))
sign_in_facebook.click()

time.sleep(3)
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
fb_user = driver.find_element(driver.by.ID, value="email")
fb_pass = driver.find_element(driver.by.ID, value="pass")
fb_user.send_keys(os.getenv("USER_NAME"))
fb_pass.send_keys(os.getenv("PASSWORD"))
fb_login = driver.find_element(driver.by.ID, value="loginbutton")
fb_login.click()

pop1 = driver.find_element(driver.by.XPATH, value='//*[@id="t-1686761967"]/div/div/div/div/div[3]/button[1]/div[2]')
time.sleep(2)
pop2 = driver.find_element(driver.by.XPATH, value='//*[@id="t-1686761967"]/div/div/div/div/'
                                                  'div[3]/button[2]/div[2]/div[2]/div')

while True:

    try:
        mark = driver.find_element(driver.by.XPATH, value='//*[@id="t41619109"]/div/div[1]/div/div/div/main/'
                                                   'div/div/div[1]/div/div[4]/div/div[2]/button/span/span')
        mark.click()
        swipes += 1

    except:
        pass


