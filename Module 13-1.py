import json
from flask import Flask, Response

app = Flask(__name__)


def check_prime_number(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/primenumber/<number>')
def is_prime_route(number):
    try:
        num = int(number)
        prime_result = check_prime_number(num)

        response = {
            "Number": num,
            "isPrime": prime_result
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=200,
                        mimetype="application/json")

    except ValueError:
        response = {
            "error": "Invalid input. Please provide a valid integer.",
            "Number": number,
            "isPrime": False
        }
        json_response = json.dumps(response)
        return Response(response=json_response, status=400,
                        mimetype="application/json")


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "error": "Invalid endpoint",
        "message": "Please use format:/primenumber/number"
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=404,
                    mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)