# Module 5-2

number0 = input("enter a number(enter space to finish the code):")
list = []


while number0 !=" ":
    number0=int(number0)
    list.append(number0)
    number0 = input("enter a number(enter space to finish the code):")

list.sort(reverse=True)
print(number0)

for i in range(0,5):
    print(list[i])


