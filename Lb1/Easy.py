from pprint import pprint
import requests


# Easy 1: GET https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20241226&json

# Easy 2:

def get_exchange_rates(date: str):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json"
    response = requests.get(url)
    if response.status_code == 200:
        return pprint(response.json())


print(get_exchange_rates("20241226"))
