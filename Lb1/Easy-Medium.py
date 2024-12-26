import matplotlib.pyplot as plt
import requests
import json
from pprint import pprint

url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241219&end=20241227&valcode=usd&json"

get_response = requests.get(url)

if get_response.status_code == 200:
    response_dictionary = json.loads(get_response.content)

    exchange_dictionary = {}
    for item in response_dictionary:
        exchange_dictionary[item['exchangedate']] = item['rate']

    # Сортування даних за датами
    exchange_dictionary = dict(sorted(exchange_dictionary.items()))

    # Побудова графіку
    fig, ax = plt.subplots()
    dates = list(exchange_dictionary.keys())
    rates = list(exchange_dictionary.values())

    ax.plot(dates, rates, marker='o', linestyle='-', color='b', label="USD")
    ax.set_title("USD Exchange Rate (UAH) Over the Week")
    ax.set_xlabel("Date")
    ax.set_ylabel("Exchange Rate (UAH)")
    ax.legend()
    plt.xticks(rotation=45, ha='right')
    plt.grid()

    plt.show()
else:
    print(f"Error fetching data: {get_response.status_code}")
