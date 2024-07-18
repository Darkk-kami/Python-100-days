import requests


class DataManager:
    def __init__(self):
        self.sheets_url = "Getyourown"
        self.customer_url = "Getyourown"
        self.data = requests.get(url=self.sheets_url).json()["prices"]
        self.city_lists = [(city["city"], city["id"]) for city in self.data]
        self.city_info = [(city["city"], city["iataCode"], city["lowestPrice"]) for city in self.data]
        self.customer_info = self.get_customer_emails()

    def update_codes(self, city_id, code):
        new_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(url=f"{self.sheets_url}/{city_id}", json=new_data)
        print(f"Updated city ID {city_id} with IATA code {code}. Response: {response.status_code}, {response.json()}")

    def get_customer_emails(self):
        user_data = requests.get(url=self.customer_url).json()["users"]
        info = [(users["whatIsYourFirstName?"],
                 users['whatIsYourEmail?']) for users in user_data]
        return info
