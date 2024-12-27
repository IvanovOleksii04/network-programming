from flask import Flask, request

application = Flask(__name__)


@application.route('/currency', methods=['GET'])
def get_currency():
    today = request.args.get('today')
    key = request.args.get('key')

    if today and key:
        return "USD - 41,5"
    else:
        return "Invalid request. Parameters 'today' and 'key' are required.", 400


if __name__ == '__main__':
    application.run(debug=True, port=8000)
