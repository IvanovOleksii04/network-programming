from bottle import route, run
@route('/')
def hello():
    return "test string(bottle)"

if __name__ == '__main__':
    run(host='localhost', port=8000)
