
(150/5)*1.12 = 33.6 

age = int(input("What age do you want to live until?\n"))
age -= int(input("What is your current age?\n"))
days = int(age * 365)
weeks = int(age * 52)
months = int(age * 12)

print(f"You have {days} days, {weeks} weeks, {months} months left")