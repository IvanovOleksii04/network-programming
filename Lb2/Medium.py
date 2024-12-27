from bottle import Bottle, request, response, run

application = Bottle()


@application.route('/data', method='GET')
def handle_headers():
    # Отримуємо заголовок Content-Type
    content_type = request.get_header('Content-Type')

    # Логіка залежно від Content-Type
    if content_type == 'application/json':
        response.content_type = 'application/json'
        return {"message": "Hello, JSON!"}
    elif content_type == 'application/xml':
        response.content_type = 'application/xml'
        return """
        <response>
            <message>Hello, XML!</message>
        </response>
        """
    else:
        response.content_type = 'text/plain'
        return "Result String!"


if __name__ == '__main__':
    run(application, host='127.0.0.1', port=8000, debug=True)
