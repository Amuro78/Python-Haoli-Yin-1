import json
from flask import Flask, Response
import mariadb

print(mariadb.__version__)
connection = mariadb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="A9deazwe",
    database="flight_game",
    autocommit=True
)

app = Flask(__name__)

def get_airport(connection, ICAO):
    try:
        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"

        cursor = connection.cursor()

        cursor.execute(sql, (ICAO,))

        result = cursor.fetchall()

        if result:
            for a in result:
                response = {
                    "ICAO": a[0],
                    "Name": a[1],
                    "Location": a[2]
                }
        json_response = json.dumps(response)
        return Response(response=json_response, status=200,
                          mimetype="application/json")



    except ValueError:

        response = {
            "error": "Invalid input. Please provide a valid ICAO code.",
        }

        json_response = json.dumps(response)
        return Response(response=json_response, status=400,
                        mimetype="application/json")

@app.route('/airport/<icao_code>')
def airport_info(icao_code):
    return get_airport(connection, icao_code)

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "error": "Invalid endpoint",
        "message": "Please use format: /airport/ZSPD"
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=404,
                    mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)