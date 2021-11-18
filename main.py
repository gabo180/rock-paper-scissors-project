import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice == 0:
  user_choice = rock
elif user_choice == 1:
  user_choice = paper
elif user_choice == 2:
  user_choice = scissors
else:
  print("ERROR, please select a number from 0 to 2(0,1,2)")

if computer_choice == 0:
  computer_choice = rock
elif computer_choice == 1:
  computer_choice = paper
else:
  computer_choice = scissors



print(user_choice)
print("\nComputer chose:\n")
print(computer_choice)


if user_choice == rock:
  if computer_choice == paper:
    print("\nYou lose!\n")
  elif computer_choice == scissors:
    print("\nYou Win!\n")
  else:
    print("\nDraw\n")

if user_choice == paper:
  if computer_choice == paper:
    print("\nDraw\n")
  elif computer_choice == scissors:
    print("\nYou lose!\n")
  else:
    print("\nYou Win!\n")

if user_choice == scissors:
  if computer_choice == paper:
    print("\nYou Win!\n")
  elif computer_choice == scissors:
    print("\nDraw\n")
  else:
    print("\nYou lose!\n")


