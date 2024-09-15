import random
Number_to_Guess = random.randint
user_choice = input("Guess the Number or Quite = ")
if(user_choice == "Quite"):
    break
if(user_choice = Number_to_Guess):
    print("Well Done!! Correct Guess.")
    break
elif(user_choice > Number_to_Guess):
    print("Your Number is Too Big , Take a smaller Guess!")
else:
    print("Your Number is Too Small , Take a Bigger Guess!")

print("<<<< ! GAME OVER ! >>>>")
