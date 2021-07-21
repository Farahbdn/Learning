print("Welcome Home, my love! Would you like to have a delicious meal made for you tonight?")

round1 = input("Yes or No? ").lower()

if round1 == "yes":
  round2 = input("What main would you like to have? Chicken or Beef? ").lower()
  if round2 == "beef":
    round3 = input("Would you like rice or mashed potatoes or salad? ").lower()
    if round3 =="rice":
      print("Aww, how did you know i wanted rice? You are the best! You know me so well! I love you! I'll cook the best dinner you'll ever have! ")
    elif round3 == "mashed potatoes":
      print("I guess that would be fine. A bit more work to do but because i love you, i'll cook it for you. But please choose rice the next time or i'll murder you in your sleep. ")
    elif round3 == "salad":
      print("Ew. You can go buy your own salad and eat, herbivore.")
    else:
      print("If you don't choose, you're not getting any dinner. You can cook yourself if you're being too picky. ")
  else:
    print("Sorry, I do not have chicken for you. You can buy your own chicken and cook it yourself.")
else:
  print("Ok, Goodbye. Go find and buy your own food. I'll be having my own fantastic meal together with my cat. :p")

