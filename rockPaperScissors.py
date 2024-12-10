import random

rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """ 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
choices = [rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
aiChoice = random.choice(choices)
print(f'Your choice:\n{choices[choice]}')
print(f'Computer chose:\n {aiChoice}')

if choices[choice] == rock and aiChoice == scissors:
    print("You win!")
elif choices[choice] == paper and aiChoice== rock:
     print('You win!')
elif choices[choice] == scissors and aiChoice == paper:
    print("You win!")
elif choices[choice] == aiChoice :
    print("Draw!")
else:
    print("You lose!")