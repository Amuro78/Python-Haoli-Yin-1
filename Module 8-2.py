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

def get_airports_by_country(connection,country_code):
    sql=f"select name, type from airport where iso_country = '{country_code}' order by type DESC"
    cursor = connection.cursor()

    cursor.execute(sql, (country_code,))
    result = cursor.fetchall()

    if result:
        print(f'Airports in {country_code}: ')
        for a in result:
            print(f'{a[0]}, {a[1]}')

    else:
        print(f'No airports found for country code {country_code}.')
    return

def run_country_program():
    get_airports_by_country(connection, country_code)
    return

country_code = input("Enter the country code (e.g., FI for Finland): ")
country_code.upper()
print(run_country_program())
