#Module 6-6
import math

def pizza():
    area1=math.pi*(0.5*diameter1)**2
    area2=math.pi*(0.5*diameter2)**2
    per_square_meter1=10000/area1*price1
    per_square_meter2=10000/area2*price2
    print(f"The price of first pizza is {per_square_meter1:.2f} per square meter.")
    print(f"The price of second pizza is {per_square_meter2:.2f} per square meter.")
    if per_square_meter1 < per_square_meter2:
        print("The first pizza is better.")
    elif per_square_meter1 == per_square_meter2:
        print("Same price.")
    else:
        print("The second pizza is better.")
        return

diameter1=int(input("Please enter the diameter(cm) of first pizza:"))
price1=int(input("Please enter the price(€) of first pizza:"))
diameter2=int(input("Please enter the diameter(cm) of second pizza:"))
price2=int(input("Please enter the price(€) of second pizza:"))
pizza()