import random


class RockPaperScissor:
    def __init__(self):
        self.options = []
        self.score = 0
        self.name = ''
        self.user = ''
        self.computer = ''
        self.point_list = []
        self.computer_win = []
        self.computer_lose = []

    def rule(self):
        self.point_list = self.options[self.options.index(self.user) + 1:]
        self.point_list.extend(self.options[:self.options.index(self.user)])
        self.computer_win = self.point_list[:int(len(self.point_list) / 2)]
        self.computer_lose = self.point_list[int(len(self.point_list) / 2):]

    def play(self):
        while True:
            # Input receiving and checking validity
            self.user = input()
            self.computer = random.choice(self.options)
            if self.user not in self.options and self.user != "!exit" and self.user != "!rating":
                print("Invalid input")
                continue
            if self.user == "!exit":
                print("Bye!")
                break
            if self.user == "!rating":
                print(f"Your rating: {self.score}")
                continue

            # Game play
            if self.user == self.computer:
                print(f"There is a draw ({self.user})")
                self.score += 50
            else:
                self.rule()
                if self.computer in self.computer_win:
                    print(f"Sorry, but the computer chose {self.computer}")
                else:
                    print(f"Well done. The computer chose {self.computer} and failed")
                    self.score += 100

    def store_result(self):
        file_1 = open("rating.txt", "r")
        for file in file_1:
            if file.split()[0] == self.name:
                self.score = int(file.split()[1])
                break
        file_1.close()

    def start(self):
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")
        self.store_result()
        self.options = input().split(",")
        if len(self.options) < 3:
            self.options = ['rock', 'paper', 'scissors']
        print("Okay, let's start")
        self.play()
        # print(self.options)  # for testing
        # print(self.score)  # for testing


# To run game
rps = RockPaperScissor()
rps.start()
