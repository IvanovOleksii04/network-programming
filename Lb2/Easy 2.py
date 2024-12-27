import random

from flask import Flask

application = Flask(__name__)


@application.route('/', methods=['GET'])
def fun1():
    return str(random.randint(0, 10))


if __name__ == '__main__':
    application.run(debug=True)
