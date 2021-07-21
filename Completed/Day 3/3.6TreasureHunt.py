print("Welcome To Treasure Island! Your Mission is to find the ultimate tressure!")

round1 = input("Left or Right? ")
round1.lower

if round1 == "left":
  round2 = input("Swim or wait? ")
  round2.lower
  if round2 == "wait":
    round3 = input("Which door? Blue, Red or Yellow? ")
    round3.lower
    if round3 =="yellow":
      print("You win a treasure! it's love! <3")
    elif round3 =="red":
      print("Burned by fire. Game Over!")
    elif round3 == "blue":
      print("Eaten by seagulls.Game Over!")
    else:
      print("You suck at this. Game over loser!")
  else:
    print("Game Over! You drown!")
else:
  print("Game Over! You died!")

