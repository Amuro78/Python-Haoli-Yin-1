# Module 5-1
import random

rounds=int(input("Enter number of rounds: "))
sum=0
for i in range(rounds):
    dice = random.randint(1, 6)
    print(dice)
    sum=sum+dice

print(f'The sum is: {sum}')
