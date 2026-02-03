#Module 7-2
names=set()

while True:
    add_name = input("Please enter the name:")

    if add_name=="":
        break

    elif add_name in names:
        print("Existing name.")

    else:
        print("New name")
        names.add(add_name)

print(names)


