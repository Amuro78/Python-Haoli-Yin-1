from geopy.distance import geodesic
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

def get_airport_coordinates(icao_code):
    sql=f"SELECT ident,name,latitude_deg,longitude_deg FROM airport WHERE ident=? "

    cursor = connection.cursor()

    cursor.execute(sql, (icao_code,))

    result = cursor.fetchall()
    if result:
        for a in result:
            loc1 = (a[2],a[3])
            return loc1



def get_airport_coordinates(icao_code1):
    sql = f"SELECT ident,name,latitude_deg,longitude_deg FROM airport WHERE ident=? "
    cursor = connection.cursor()

    cursor.execute(sql, (icao_code1,))

    result = cursor.fetchall()
    if result:
        for a in result:
            loc2 = (a[2], a[3])
            return loc2

def run_airport_distance():
    dist = geodesic(get_airport_coordinates(icao_code),get_airport_coordinates(icao_code1)).km
    return (f"Distance between {icao_code} and {icao_code1}: {dist:.2f} kilometers")



icao_code = input("Enter the ICAO code of the first airport: ")
icao_code1= input("Enter the ICAO code of the second airport: ")
icao_code.upper()
icao_code1.upper()
print(run_airport_distance())
