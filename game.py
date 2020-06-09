import random


class RockPaperScissors:

    def __init__(self, name, options, decision):
        self.name = name
        self.options = options
        self.decision = decision
        self.score = 0
        self.lose_conditions = {}

    def user_beat_options(self):
        half = len(self.options) // 2
        for action in self.options:
            if half <= self.options.index(action):
                start = self.options.index(action) - half
                end = self.options.index(action)
                self.lose_conditions[action] = self.options[start:end]
            else:
                first_end = self.options.index(action)
                second_half = first_end - half
                self.lose_conditions[action] = self.options[0:first_end] + self.options[second_half:]

    def get_score(self):
        file = open("rating.txt", "r", encoding="utf-8")

        for line in file:
            if self.name in line:
                record = line.split()
                self.score = int(record[1])
        file.close()

    def play_game(self):
        while self.decision != "!exit":
            computer_input = random.choice(self.options)
            if self.decision in self.options:
                if self.decision in computer_input:
                    print(f"There is a draw ({computer_input})")
                    self.score += 50
                elif computer_input in self.lose_conditions[self.decision]:
                    print(f"Well done. Computer chose {computer_input} and failed")
                    self.score += 100
                else:
                    print(f"Sorry, but computer chose {computer_input}")
            elif self.decision == "!rating":
                print(self.score)
            else:
                print("Invalid input")
            self.decision = input()
        print("Bye!")


input_name = input("Enter your name: ")
print(f"Hello, {input_name}")

test_input = input()
if test_input == "":
    test_input = "rock,paper,scissors"
input_options = test_input.split(",")
print("Okay, let's start")

input_decision = input()

player = RockPaperScissors(input_name, input_options, input_decision)
player.get_score()
player.user_beat_options()
player.play_game()
