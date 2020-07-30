theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '}

win = (('top-l', 'top-m', 'top-r'), ('mid-l', 'mid-m', 'mid-r'), ('low-l', 'low-m', 'low-r'),
        ('top-l', 'mid-m', 'low-r'), ('top-r', 'mid-m', 'low-l'))


def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print("-+-+-")
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print("-+-+-")
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])


def wygrana(board):
    won = False
    if board(win):
        won = True
    return won

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space ?(top-L,mid-M itp')
    move = input()
    theBoard[move] = turn
    won = wygrana(theBoard)
    if won:
        print(turn + ' wins the game!')
        break
    elif turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

