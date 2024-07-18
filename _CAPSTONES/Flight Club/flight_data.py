class FlightData:
    def __init__(self, lowest_price, origin, destination, departure, return_date, stops):
        self.price = lowest_price
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(result):

    if result is None or not result['data']:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A",
                          "N/A", 'N/A')

    first_flight = result['data'][0]
    stops = len(first_flight["itineraries"][0]["segments"]) - 1
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, departure, return_date, stops)

    for flight in result["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
