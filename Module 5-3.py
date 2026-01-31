num=int(input("Please enter an integer:"))

if num <= 1:
    print(f'{num} is not a prime numer.')


for i in range(2,num+1):
    if num == 2:
        print(f"{num} is prime!")
        break

    if num%i== 0:
        print(f"{num} is not a prime number.")
        break

    elif num%i!= 0 :
        print(f"{num} is prime!")
        break

