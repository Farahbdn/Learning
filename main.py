# (150/5)*1.12 = 33.6 

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? \n 10, 12 or 15?\n"))
no_of_people = int(input("How many people to split the bill? "))
#bill = "{:2f}".format(total_bill)

Result = round((total_bill/no_of_people) * (1+ (percentage/100)),2)

print(f"Each person should pay: ${Result}") 

# print(Result)