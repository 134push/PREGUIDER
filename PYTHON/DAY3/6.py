## rock and paper game 
import random

user_point = 0
machine_point = 0
i = 0
list = ["rock", "paper", "scissors"]
machine_choice = random.randint(0, len(list) - 1)

while (i < 5):
    print(f"round no {i + 1}")
    user_choice = input("what is your choice? rock, paper or scissors? ").lower()
    print(f"user choice is: {user_choice}")
    if user_choice == list[machine_choice]:
        print("it's a tie")
    elif user_choice == "rock" and list[machine_choice] == "scissors":
        print("you win")
        user_point += 1
    elif user_choice == "rock" and list[machine_choice] == "paper":
        print("you lose")
        machine_point += 1
    elif user_choice == "paper" and list[machine_choice] == "rock":
        print("you win")
        user_point += 1
    elif user_choice == "paper" and list[machine_choice] == "scissors":
        print("you lose")
        machine_point += 1
    elif user_choice == "scissors" and list[machine_choice] == "paper":
        print("you win")
        user_point += 1
    elif user_choice == "scissors" and list[machine_choice] == "rock":
        print("you lose")
        machine_point += 1
    elif user_choice not in list:
        print("invalid choice")
  
    i += 1

print(f"user point is: {user_point}")
print(f"machine point is: {machine_point}")
