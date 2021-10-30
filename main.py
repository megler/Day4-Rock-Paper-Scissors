# rockPaperScissors.py
#
# Python Bootcamp Day 4 - Rock, Paper, Scissors
# Usage:
#      Decision making with rock, paper, scissors
#
# Marceia Egler Sept 24, 2021



#import random module
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

#Ask user for their choice and convert to integer
user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

#put drawings in array
drawing = [rock, paper, scissors]

#computer makes a choice
comp_choice = random.randint(0,2)

if user_choice > 2 or user_choice < 0:
  print("Invalid selection. You lose")
elif user_choice == comp_choice:
  print(f"""{drawing[user_choice]}  \nComputer chose:\n  {drawing[comp_choice]}  \nYou tie!""") 
elif comp_choice == user_choice + 1 or comp_choice == user_choice - 2 :
  print(f"""{drawing[user_choice]}  \nComputer chose:\n  {drawing[comp_choice]}  \nYou lose!""")
else:
  print(f"""{drawing[user_choice]}  \nComputer chose:\n  {drawing[comp_choice]}  \nYou win!""")
