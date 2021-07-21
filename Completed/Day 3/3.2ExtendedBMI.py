weight = float(input("Weight:\n"))
height = float(input("Height:\n"))

BMI = round((weight / (height * height)))

if BMI < 18.5:
  if BMI <= 25:
    print (f"Your BMI is {BMI}, and You have a normal weight")
  elif BMI <= 30:
    print(f"Your BMI is {BMI},You are overweight") 
  elif BMI <= 35:
    print(f"Your BMI is {BMI},You are obese! Go exercise")
  else:
    print(f"Your BMI is {BMI},You are clinically obese")
else:
    print (f"Your BMI is {BMI}, You're underweight")

# print(round(BMI,2))
# print(f"Your BMI is{BMI}, and  )