import random

theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'bot-l': ' ', 'bot-m': ' ', 'bot-r': ' '}


def printBoard(board):
    print(board['top-l'] + '|'+board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['bot-l'] + '|' + board['bot-m'] + '|' + board['bot-r'])


def inputLetter():
    letter = ''
    while not letter == 'X' or letter == 'O':
        print('Do you want to be X or O ?')
        letter = input().upper() # upper - because it has to be big X
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoisfirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    print('Do you want to play again? - type yes or no')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


printBoard(theBoard)
