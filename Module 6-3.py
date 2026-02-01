# Module 6-3

def quantity(gallon):
    liter=gallon*3.79
    return liter

while True:
 gallon=float(input("Please enter a number of quantity(American gallon):"))
 liter=quantity(gallon)
 if liter < 0:
    print("Please enter a valid number.")
    break
 print(f"the liter is {liter:.2f} ")









