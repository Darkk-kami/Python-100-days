import requests


class FlightSearch:
    def __init__(self):
        self.api_key = "Getyourown"
        self.api_secret = "Getyourown"
        self.token = self.get_new_token()

    def get_new_token(self):

        header = {
            "Content-Type": 'application/x-www-form-urlencoded',
        }

        auth_params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret,
        }

        return requests.post(url='https://test.api.amadeus.com/v1/security/oauth2/token',
                             data=auth_params, headers=header, verify=False).json()["access_token"]

    def search_city(self, city_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        try:
            iata_code = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
                                     params=query, headers=headers, verify=False).json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        print(f"{iata_code}")
        return iata_code

    def check_flight(self, origin, destination, tomorrow, return_date, is_direct=True):
        headers = {"Authorization": f"Bearer {self.token}"}

        query = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": tomorrow,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers",
                                params=query, headers=headers, verify=False).json()

        return response
