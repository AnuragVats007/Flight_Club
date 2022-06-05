import requests

SHEETY_USER = "neophyte"
SHEETY_PASS = "password_of_auth"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.price_endpoint = "https://api.sheety.co/6c78f80074b9681485512fe11f15a129/flightDeals/prices"

        self.response = requests.get(url=self.price_endpoint, auth=(SHEETY_USER, SHEETY_PASS))
        # print(self.response.status_code)
        self.data = self.response.json()
        # print(self.data)

    def get_flight_data(self):
        return self.data

    def get_user_data(self):
        self.users_endpoint = "https://api.sheety.co/6c78f80074b9681485512fe11f15a129/flightDeals/users"
        self.res = requests.get(url=self.users_endpoint, auth=(SHEETY_USER, SHEETY_PASS))
        self.user_data = self.res.json()
        return self.user_data

    def set_user(self,fname,lname,email):
        self.users_endpoint_post = "https://api.sheety.co/6c78f80074b9681485512fe11f15a129/flightDeals/users"
        self.input_details = {
            "user":{
                "firstname":fname,
                "lastname":lname,
                "email":email,
            }
        }
        resp = requests.post(url=self.users_endpoint_post, json=self.input_details, auth=(SHEETY_USER, SHEETY_PASS))
        # print(resp.status_code)
        # print(resp.json())
        # print(resp.text)

    
    