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

def get_airport(connection,ICAO):
    sql=f"SELECT ident,name,municipality FROM airport WHERE ident= ?"

    cursor = connection.cursor()

    cursor.execute(sql, (ICAO,))

    result = cursor.fetchall()

    if result:
        for a in result:
            print(f'Airport name:{a[1]}, Location:{a[2]} ')

    else:
        print(f'No record found with ICAO code')


ICAO = input("Enter the ICAO code of an airport: ")
ICAO.upper()
get_airport(connection,ICAO)