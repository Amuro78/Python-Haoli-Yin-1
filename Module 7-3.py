# Module 7-3

airports={"EFHK":"Finland-Helsinki-Vantaa",
          "RKNC":"Korea-A-306"}

while True:
    print("Number 1 for enter a new airport. \nNumber 2 for fetch airport information. "
          "\nNumber 3 for quit.")
    name=int(input("Please enter the number:"))
    if name==1:
        print("1.Enter a new airport.")
        ICAO_code=input("Please enter the ICAO code:")
        name_airport=input("Please enter the name of the airport:")
        airports[ICAO_code]=name_airport

    elif name==2:
        print("2.Fetch airport information.")
        search_ICAO_code=input("Please enter the ICAO code:")
        print(f"The {search_ICAO_code} for {airports[search_ICAO_code]}")

    elif name==3:
        print("3.Exit.")
        break