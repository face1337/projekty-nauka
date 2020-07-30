# Rock, paper, scissors game
import random


def game_code():
    print('How many rounds to win?')
    win_rounds = int(input())
    player_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']
    print('Rock, paper or scissors ?')
    while player_score != win_rounds and computer_score != win_rounds:
        ans = str(input())
        computer = random.choice(options)
        print('Rock, paper or scissors ?')
        if ans == options[0] and computer == options[2]:
            player_score += 1
            print('Your score : ' + str(player_score) + ' Computer score : ' + str(computer_score))
        elif ans == options[1] and computer == options[0]:
            player_score += 1
            print('Your score : ' + str(player_score) + ' Computer score : ' + str(computer_score))
        elif ans == options[2] and computer == options[1]:
            player_score += 1
            print('Your score : ' + str(player_score) + ' Computer score : ' + str(computer_score))
        elif ans == computer:
            print('You and computer have chosen ' + str(ans) + ' , Try again')
            continue
        else:
            computer_score += 1
            print('Your score : ' + str(player_score) + ' Computer score : ' + str(computer_score))
    if computer_score == win_rounds:
        print('Computer won.')
    else:
        print('You won!')


try:
    game_code()
except ValueError:
    print('Error : You did not enter an integer value')
