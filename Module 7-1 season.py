#Module 7-1
whole_year=("January","February","March","April","May","June","July","August",
            "September","October","November","December")
seasons="spring","summer","autumn","winter"

input_month=int(input("Please enter a number of month:"))
if input_month in (3,4,5):
    season = seasons[0]

elif input_month in (6,7,8):
    season = seasons[1]

elif input_month in (9,10,11):
    season = seasons[2]

elif input_month in (12,1,2):
    season = seasons[3]

month1=whole_year[input_month-1]
print(f"{month1} is {season}. ")

