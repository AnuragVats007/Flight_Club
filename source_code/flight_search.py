import requests

FROM_CITY = "LON"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass
    def get__(self, flyTo, fromdate,todate) -> None:
        self.flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        # asd = "https://tequila-api.kiwi.com/v2/search?apikey=gEJj34fofvhqib3jOdrkA_MMAkiiuGLG&fly_from=DEL&fly_to=BOM&dateFrom=20/12/2021&dateTo=20/01/2022"

        self.fly_to = flyTo
        self.from_date = fromdate
        self.to_date = todate

        self.header = {
            "apikey":"gEJj34fofvhqib3jOdrkA_MMAkiiuGLG",
        }
        self.flight_search_params = {
            "fly_from":FROM_CITY,
            "fly_to":self.fly_to,
            "dateFrom":self.from_date,
            "dateTo":self.to_date,
        }
        response = requests.get(url=self.flight_search_endpoint,headers=self.header, params=self.flight_search_params)
        # print(response.status_code)
        return response.json()