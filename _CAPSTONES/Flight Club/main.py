import notification_manager
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager

ORIGIN = "LON"
TOMORROW = dt.date.today() + dt.timedelta(days=1)
RETURN = dt.date.today() + dt.timedelta(days=6*30)

data_manager = DataManager()
search = FlightSearch()

# # for city in data_manager.city_lists:
# #     code = search.search_city(city[0])
# #     city_id = city[1]
# #     data_manager.update_codes(city_id=city_id, code=code)


for destinations in data_manager.city_info:
    print(f"Getting flights for {destinations[0]}...")
    result = search.check_flight(origin=ORIGIN, destination=destinations[1],
                                 tomorrow=TOMORROW, return_date=RETURN)
    alert = find_cheapest_flight(result)
    print(f"{alert.destination}: £{alert.price}")

    if alert.price == 'N/A':
        print(f"Getting indirect flights for {destinations[0]}...")
        result = search.check_flight(origin=ORIGIN, destination=destinations[1],
                                     tomorrow=TOMORROW, return_date=RETURN, is_direct=False)
        alert = find_cheapest_flight(result)

    if alert.price != 'N/A' and float(alert.price) < float(destinations[2]):

        if alert.stops == 0:
            message = (f"Low Price Alert!!! catch a Direct flight from:\n{destinations[0]},"
                       f"{alert.destination} at £{alert.price} on {alert.departure}")
        else:
            message = (f"Low Price Alert!!! catch a flight with {alert.stops} stops from:\n{destinations[0]},"
                       f"{alert.destination} at £{alert.price} on {alert.departure}")

        notification_manager.NotificationManager().send_sms(message_body=message)
        notification_manager.NotificationManager().send_emails(email_list=data_manager.customer_info,
                                                               email_body=message)
