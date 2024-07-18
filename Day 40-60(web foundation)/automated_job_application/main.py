from driver import Driver
import os
import dotenv
import time

dotenv.load_dotenv()

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=397177"
       "9738&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")


driver = Driver()
driver.get(URL)

sign_in = driver.find_element(driver.by.LINK_TEXT, value="Sign in")
sign_in.click()

username = driver.find_element(driver.by.ID, value="username")
username.send_keys(f'{os.getenv("USER_NAME")}')
password = driver.find_element(driver.by.ID, value="password")
password.send_keys(f'{os.getenv("PASSWORD")}')
sign_in2 = driver.find_element(driver.by.CSS_SELECTOR, value="div button")
sign_in2.click()


for job in range(0, 24):
    job_listing = driver.wait(driver, 10).until(driver.EC.presence_of_all_elements_located(
        (driver.by.CSS_SELECTOR, ".scaffold-layout__list-container strong")))

    apply = driver.wait(driver, 10).until(driver.EC.presence_of_all_elements_located((driver.by.CSS_SELECTOR,
                                                                                      "div.mt5 button")))
    driver.execute_script("arguments[0].scrollIntoView(true);", job_listing[job])
    apply[1].click()
    print("applied")
    job_listing[job].click()
    print("clicked")
    time.sleep(5)
