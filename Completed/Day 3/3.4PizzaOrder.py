
size = input("What size would you like? S , M or L?  ")

add_pepp = input("Would you like pepporoni? Y or N? ")

add_cheese = input("Would you like cheese? Y or N? ")

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill +=20
elif size == "L":
  bill +=25


if add_pepp == "Y":
  if size == "S":
    bill += 2
  else:
    bill +=3

if add_cheese == "Y":
  bill += 1

print (f"Your bill is ${bill}! Please pay now")













# # small_pizza = 15
# # medium_pizza = 20
# # large_pizza = 25
# bill = 0

# size = input("What size would you like? S , M or L?  ")

# if size != "S":
#     if size == "M":
#       bill +=20
#       # print (f"Your bill is {bill}! Please pay now")
#     elif size == "L":
#       bill +25
#       # print (f"Your bill is {bill}! Please pay now")
    
#     want_pepp = input("Would you like pepporoni? Y or N? ")  
#     if want_pepp == "Y":
#       bill +=3
#       print (f"Your bill is ${bill}! Please pay now")
#     else:
#       print (f"Your bill is ${bill}! Please pay now")
    
# else:
#   bill = 15
#     # print (f"Your bill is {bill}! Please pay now")
  
#   want_pepp = input("Would you like pepporoni? Y or N? ")  
#   if want_pepp == "Y":
#     bill +=2
#     print (f"Your bill is ${bill}! Please pay now")
#   else:
#     print (f"Your bill is ${bill}! Please pay now")


