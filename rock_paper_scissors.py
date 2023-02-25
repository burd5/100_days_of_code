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

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
computer_choice = random.randint(0,2)

if user_choice == 0:
    if computer_choice == 0:
        print(f"You chose:\n{rock}\nComputer chose:\n{choices[computer_choice]}\nTie: Try Again")
    elif computer_choice == 1:
        print(f"You chose:\n{rock}\nComputer chose:\n{choices[computer_choice]}\nYou lose.")
    elif computer_choice == 2:
        print(f"You chose:\n{rock}\nComputer chose:\n{choices[computer_choice]}\nYou win.")
        
if user_choice == 1:
    if computer_choice == 0:
        print(f"You chose:\n{paper}\nComputer chose:\n{choices[computer_choice]}\nYou win.")
    elif computer_choice == 1:
        print(f"You chose:\n{paper}\nComputer chose:\n{choices[computer_choice]}\nTie: Try Again")
    elif computer_choice == 2:
        print(f"You chose:\n{paper}\nComputer chose:\n{choices[computer_choice]}\nYou lose.")

if user_choice == 2:
    if computer_choice == 0:
        print(f"You chose:\n{scissors}\nComputer chose:\n{choices[computer_choice]}\nYou lose.")
    elif computer_choice == 1:
        print(f"You chose:\n{scissors}\nComputer chose:\n{choices[computer_choice]}\nYou win.")
    elif computer_choice == 2:
        print(f"You chose:\n{scissors}\nComputer chose:\n{choices[computer_choice]}\nTie: Try Again")
