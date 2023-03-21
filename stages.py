# Stage 3/5: Endless game
# rock beats scissors, paper wins over rock, scissors defeats paper.
import random


class RockPaperScissors:
    def __init__(self):
        self.user, self.computer = "", ""

    def play(self):
        self.computer = random.choice(["rock", "scissors", "paper"])
        if self.user == self.computer:
            print(f"There is a draw ({self.user})")
        elif self.user == "rock" and self.computer == "scissors":
            print("Well done. The computer chose scissors and failed")
        elif self.user == "rock" and self.computer == "paper":
            print("Sorry, but the computer chose paper")
        elif self.user == "scissors" and self.computer == "rock":
            print("Sorry, but the computer chose rock")
        elif self.user == "scissors" and self.computer == "paper":
            print("Well done. The computer chose paper and failed")
        elif self.user == "paper" and self.computer == "scissors":
            print("Sorry, but the computer chose scissors")
        elif self.user == "paper" and self.computer == "rock":
            print("Well done. The computer chose rock and failed")

    def start(self):
        while True:
            self.user = input()
            if self.user == "!exit":
                print("Bye!")
                break
            elif self.user in ["rock", "scissors", "paper"]:
                self.play()
            else:
                print("Invalid input")


rps = RockPaperScissors()
rps.start()
