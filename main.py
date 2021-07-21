
# Angela Yu
#  Jack Bauer
# 53%

name1 = input("What is the your name? \n")
name2 = input ("What is your significant's name?\n")

name1.lower 
name2.lower

combine_name = (name1 + " " + name2) 

# true love 
t = int(combine_name.count("t"))
r = int(combine_name.count("r"))
u = int(combine_name.count("u"))
e = int(combine_name.count("e"))
l = int(combine_name.count("l"))
o = int(combine_name.count("o"))
v = int(combine_name.count("v"))

result1 = (t+r+u+e)
result2 = (l+o+v+e)
score = (result1*10) + result2

# print(type(result1))

# print(f"Your love score is {score}%")

# print(type(result2))

# if score >=10:
#   if score <40: #btwn 10 & 40
#     print(f" Your score is {score}%. Nothing much")

#   elif score <=50: #btwn 40 & 50
#     print(f"Your score is {score}%, you are alright togther")

#   elif score <=90:
#     print(f" Your score is {score}%. Nothing much")
  
#   else:
#     print(f"Your score is {score}%, you go together like coke and mentos." )
# else:
#   print(f" Your score is {score}%. Nothing much")


if score < 10 or score >90:
  print(f"Your score is {score}%, you go together like coke and mentos." )
elif score >=40 and score <=50:
  print(f"Your score is {score}%, you are alright togther")
else:
  print(f" Your score is {score}%. Nothing much")