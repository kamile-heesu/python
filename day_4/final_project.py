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

import random;

hand_gesture = [rock, paper, scissors];

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n" ))



computer_pick = random.randint(0, 2);

if user_pick >= 3 or user_pick < 0:
  print("Out of Range")
else:
  print(f"Your hand :\n {hand_gesture[user_pick]}")
  print(f"Computer's : \n {hand_gesture[computer_pick]}")
  if user_pick < computer_pick:
    print("You loose");
  elif computer_pick < user_pick:
    print("You win");
  elif user_pick == 0 and computer_pick == 2:
    print("You win");
  elif computer_pick == 0 and user_pick == 2:
    print("You loose");
  elif user_pick == computer_pick:
    print("It's a draw");
  
