# Stage 2/5: Equalizing chances
import random


user = input()
computer = random.choice(["rock", "scissors", "paper"])
if user == computer:
    print(f"There is a draw ({user})")
elif user == "rock" and computer == "scissors":
    print("Well done. The computer chose scissors and failed")
elif user == "rock" and computer == "paper":
    print("Sorry, but the computer chose paper")
elif user == "scissors" and computer == "rock":
    print("Sorry, but the computer chose rock")
elif user == "scissors" and computer == "paper":
    print("Well done. The computer chose paper and failed")
elif user == "paper" and computer == "scissors":
    print("Sorry, but the computer chose scissors")
elif user == "paper" and computer == "rock":
    print("Well done. The computer chose rock and failed")
    