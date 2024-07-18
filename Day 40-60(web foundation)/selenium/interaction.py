from selenium.common import StaleElementReferenceException, NoSuchElementException
from driver import Driver

import time
URL = "https://orteil.dashnet.org/experiments/cookie/"

driver = Driver()
driver.get(URL)

cookie = driver.find_element(driver.by.ID, value="cookie")

end_time = time.time() + 60 * 5


def get_money():
    money = driver.find_element(driver.by.ID, value="money")
    money = int(money.text.replace(",", ""))
    return money


game_on = True

while game_on and time.time() < end_time:
    try:
        store = driver.find_elements(driver.by.CSS_SELECTOR, value="#store b")[:-1]
        item_prices = [int(item.text.split(" ")[-1].replace(",", "")) for item in store if item.text]
        cookie.click()
        current_money = get_money()
        lowest_price = min(item_prices)
        lowest_price_index = item_prices.index(lowest_price)

        if current_money > lowest_price:
            store[lowest_price_index].click()
            print(f"Bought item for {lowest_price} cookies.")
    except (StaleElementReferenceException, NoSuchElementException):
        # Refresh elements
        continue

