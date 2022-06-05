from flight_search import *

class FlightData:
    #This class is responsible for structuring the flight data.
    def chk(self, flight_info,lowestprice):
        print(lowestprice)
        # print(flight_info)
        self.lp = flight_info["data"][0]["price"]
        # print(self.lp)
        self.seats = flight_info["data"][0]["availability"]["seats"]
        # print(self.seats)
        self.city = flight_info["data"][0]["cityTo"]
        # print(self.city)
        self.local_arrival = flight_info["data"][0]["local_arrival"]
        # print(self.local_arrival)
        # print(type(self.local_arrival))
        self.dept = flight_info["data"][0]["local_departure"]
        # print(self.dept)
        if self.lp<=lowestprice and self.seats>0:
            return True
        else:
            return False

    def get_msg(self):
        return f"Seats are available in a flight to {self.city} at a price of {self.lp}.\nDate of arrival: {self.local_arrival}\nDate of departure: {self.dept}"