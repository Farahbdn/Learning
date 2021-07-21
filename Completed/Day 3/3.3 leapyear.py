
year = int(input("Enter a year: "))

if (year % 4) !=0:
  if (year %100) != 0:
    print("It is not a leap year! 365 days!")
  elif (year % 400) != 0:
    print("It is not a leap year! 365 days!")
else:   
  print("It is a leap year! 366 days")

#https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year 