number=int(input("Please enter an integer:"))

if number <= 1 or number==4:
    print(f'{number} is not a prime numer.')

elif number == 2 or number==3 or number==5:
    print(f"{number} is prime!")


for i in range(6,number):

    if number % 2== 0 or number % 3==0 or number % 5==0:
        print(f"{number} is not a prime number.")
        break

    else:
        print(f"{number} is a prime number!")
        break




