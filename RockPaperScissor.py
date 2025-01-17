import random
import time

from pip._vendor.distlib.compat import raw_input

rock = 1
paper = 2
scissor = 3

names = {rock: "Rock", paper: "Paper", scissor: "Scissor"}
rules = {rock: scissor, paper: rock, scissor: paper}

player_score = 0
computer_score = 0


def start():
    print("Let's play a game of Rock, paper, Scissors.")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        print()
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3 \n\nMake a move:- ")
        try:
            player = int(player)
            if player in {1, 2, 3}:
                return player
        except ValueError:
            pass
            print("Oops! I didn't understand. Please enter 1, 2 or 3")


def result(player, computer):
    print("1......")
    time.sleep(1)
    print("2......")
    time.sleep(1)
    print("3!")
    time.sleep(0.5)
    print("Computer threw {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie Game")
    else:
        if rules[player] == computer:
            print("Your victory has been assured")
            player_score += 1
        else:
            print("The computer laughs as you realize you have been defeated")
            computer_score += 1


def play_again():
    answer = input("Would you like to play again? Y/N")
    if answer in {"Y", "y", "yes"}:
        return answer
    else:
        print("Thank you")


def scores():
    global player_score, computer_score
    print("High Scores")
    print("PLayers:- ", player_score)
    print("Computer:- ", computer_score)


if __name__ == '__main__':
    start()
