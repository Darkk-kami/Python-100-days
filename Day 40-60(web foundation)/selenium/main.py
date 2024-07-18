from driver import Driver
URL = 'https://www.python.org/'

driver = Driver()
driver.get(URL)

price = driver.find_element(driver.by.CLASS_NAME, value="medium-widget.event-widget")

event_list = price.text.split("\n")[2::]
print(event_list)

event_dict = {}
for i in range(0, len(event_list) - 1, 2):
    event_dict[f"{i//2}"] = {
        "time": event_list[i],
        "event": event_list[i + 1]
    }

print(event_dict)
driver.quit()
