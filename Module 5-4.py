# Module 5-4
cities=[]

for i in range(1,6):
    city = input(f"You need enter the names of {i} cities:")
    cities.append(city)
print("You have entered five cities:",cities)
print("You have entered cities:")

for city in cities:
    print(city)


