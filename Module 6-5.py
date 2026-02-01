# Module 6-5

even_numbers=[]
def numbers(list):
   for i in list:
    if i % 2==0:
       even_numbers.append(i)
   return even_numbers

list=[1,11,21,63,2,3,4,5,6,70,86]
print("The original list:",list)
even_numbers_fin=numbers(list)
print("The even numbers list:", even_numbers_fin)

