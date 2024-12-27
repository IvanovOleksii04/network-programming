from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta


'''

today = http://127.0.0.1:8000/currency?param=today
yesterday = http://127.0.0.1:8000/currency?param=yesterday

'''
application = Flask(__name__)

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


def get_usd_rate(date):
    """
    Запит до API НБУ для отримання курсу USD на задану дату.
    """
    response = requests.get(NBU_API_URL, params={"date": date.strftime("%Y%m%d")})
    if response.status_code == 200:
        data = response.json()
        for currency in data:
            if currency["cc"] == "USD":
                return currency["rate"]
    return None


@application.route('/currency', methods=['GET'])
def get_currency_rate():
    # Отримуємо параметр
    param = request.args.get('param')

    # Обробка параметра
    if param == "today":
        today = datetime.now()
        rate = get_usd_rate(today)
    elif param == "yesterday":
        yesterday = datetime.now() - timedelta(days=1)
        rate = get_usd_rate(yesterday)
    else:
        return jsonify({"error": "Invalid parameter. Use 'today' or 'yesterday'."}), 400

    # Якщо курс не знайдено
    if rate is None:
        return jsonify({"error": "Unable to fetch exchange rate."}), 500

    # Повертаємо результат
    return jsonify({"USD_rate": rate})


if __name__ == '__main__':
    application.run(debug=True, port=8000)
