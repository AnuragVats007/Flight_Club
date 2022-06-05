# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import *
from data_manager import *
from flight_data import *
from notification_manager import *
from datetime import datetime

sheety_obj = DataManager()
flight_obj = FlightSearch()
flighi_data_obj = FlightData()
notify_obj = NotificationManager()


date_now = datetime.now()
fromdate = date_now.strftime("%d/%m/%Y")
if date_now.month>6:
    mon = date_now.month-6
    yr = date_now.year+1
else:
    mon = date_now.month+6
    yr = date_now.year
to_date = datetime(year=yr, month=mon, day=date_now.day)
to_date = to_date.strftime("%d/%m/%Y")

data = sheety_obj.get_flight_data()
user_data = sheety_obj.get_user_data()
for item in data["prices"]:
    name = item["city"]
    iata = item["iataCode"]
    lp = item["lowestPrice"]
    flight_info = flight_obj.get__(iata,fromdate,to_date)
    if flighi_data_obj.chk(flight_info, lp):
        msg = flighi_data_obj.get_msg()
        for info in user_data["users"]:
            notify_obj.notify(info["email"],msg)



