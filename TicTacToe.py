from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print(  '+-------+-------+-------+',\
            '|       |       |       |',\
            '|   '+str(board[0][0])+'   |   '+str(board[0][1])+'   |   '+str(board[0][2])+'   |',\
            '|       |       |       |',\
            '+-------+-------+-------+',\
            '|       |       |       |',\
            '|   '+str(board[1][0])+'   |   '+str(board[1][1])+'   |   '+str(board[1][2])+'   |',\
            '|       |       |       |',\
            '+-------+-------+-------+',\
            '|       |       |       |',\
            '|   '+str(board[2][0])+'   |   '+str(board[2][1])+'   |   '+str(board[2][2])+'   |',\
            '|       |       |       |',\
            '+-------+-------+-------+',sep='\n')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    freeList = make_list_of_free_fields(board)

    while True:
        try:
            playerSelection = int(input("Please enter your move: "))
            for i in range(3):
                for j in range(3):
                    if board[i][j] == playerSelection:
                        board[i][j] = 'O'
                        display_board(board)
                        return
            if playerSelection < 1 or playerSelection > 9:
                print("You didn't enter a valid number.  Please try again.")
            else:
                print("You have entered a non-empty space.  Please try again.")
        except:
            print("You didn't enter a valid number.  Please try again.")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    freeList = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                freeList.append((i,j))
    return freeList

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game

    # Row Win Case
    if (board[0][0] == 'X')\
        and (board[0][1] == 'X')\
        and (board[0][2] == 'X')\
        and (sign == 'X'):
        victoryFlag = 1
    elif (board[1][0] == 'X')\
        and (board[1][1] == 'X')\
        and (board[1][2] == 'X')\
        and (sign == 'X'):
        victoryFlag = 1
    elif (board[2][0] == 'X')\
        and (board[2][1] == 'X')\
        and (board[2][2] == 'X')\
        and (sign == 'X'):
        victoryFlag = 1
    elif (board[0][0] == 'O')\
        and (board[0][1] == 'O')\
        and (board[0][2] == 'O')\
        and (sign == 'O'):
        victoryFlag = 2
    elif (board[1][0] == 'O')\
        and (board[1][1] == 'O')\
        and (board[1][2] == 'O')\
        and (sign == 'O'):
        victoryFlag = 2
    elif (board[2][0] == 'O')\
        and (board[2][1] == 'O')\
        and (board[2][2] == 'O')\
        and (sign == 'O'):
        victoryFlag = 2
    else:
        victoryFlag = 0
    
    if victoryFlag != 0:
        return victoryFlag
    
    # Column Win Case
    if (board[0][0] == 'X')\
        and (board[1][0] == 'X')\
        and (board[2][0] == 'X')\
        and (sign == 'X'):
        victoryFlag = 3
    elif (board[0][1] == 'X')\
        and (board[1][1] == 'X')\
        and (board[2][1] == 'X')\
        and (sign == 'X'):
        victoryFlag = 3
    elif (board[0][2] == 'X')\
        and (board[1][2] == 'X')\
        and (board[2][2] == 'X')\
        and (sign == 'X'):
        victoryFlag = 3
    elif (board[0][0] == 'O')\
        and (board[1][0] == 'O')\
        and (board[2][0] == 'O')\
        and (sign == 'O'):
        victoryFlag = 4
    elif (board[0][1] == 'O')\
        and (board[1][1] == 'O')\
        and (board[2][1] == 'O')\
        and (sign == 'O'):
        victoryFlag = 4
    elif (board[0][2] == 'O')\
        and (board[1][2] == 'O')\
        and (board[2][2] == 'O')\
        and (sign == 'O'):
        victoryFlag = 4
    else:
        victoryFlag = 0
    
    if victoryFlag != 0:
        return victoryFlag
    
    # TL-BR Diagonal Win Case
    if (board[0][0] == 'X')\
        and (board[1][1] == 'X')\
        and (board[2][2] == 'X')\
        and (sign == 'X'):
        victoryFlag = 5
    elif (board[0][0] == 'O')\
        and (board[1][1] == 'O')\
        and (board[2][2] == 'O')\
        and (sign == 'O'):
        victoryFlag = 6
    else:
        victoryFlag = 0
    
    if victoryFlag != 0:
        return victoryFlag
    
    # BL-TR Diagonal Win Case
    if (board[0][2] == 'X')\
        and (board[1][1] == 'X')\
        and (board[2][0] == 'X')\
        and (sign == 'X'):
        victoryFlag = 7
    elif (board[0][2] == 'O')\
        and (board[1][1] == 'O')\
        and (board[2][0] == 'O')\
        and (sign == 'O'):
        victoryFlag = 8
    else:
        victoryFlag = 0
    
    return victoryFlag

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    freeList = make_list_of_free_fields(board)
    
    if len(freeList) == 9:
        board[1][1] = 'X'
    else:
        pick = randrange(len(freeList))
        target = freeList[pick]
        freeRow = target[0]
        freeCol = target[1]
        board[freeRow][freeCol] = 'X'
    
    display_board(board)


# Game Loop
global board
board = [[1,2,3],[4,5,6],[7,8,9]]
global victoryFlag
victoryFlag = 0
global turnCount
turnCount = 0


while turnCount < 9 and victoryFlag == 0:
    draw_move(board)
    turnCount += 1
    victoryFlag = victory_for(board,'X')
    if turnCount == 9 or victoryFlag != 0:
        break
    enter_move(board)
    victoryFlag = victory_for(board,'O')
    turnCount += 1

if victoryFlag == 1:
    print("The CPU wins by three-in-a-row!")
elif victoryFlag == 2:
    print("You won by three-in-a-row!")
elif victoryFlag == 3:
    print("The CPU wins by three-in-a-column!")
elif victoryFlag == 4:
    print("You won by three-in-a-column!")
elif victoryFlag == 5:
    print("The CPU wins by top-left to bottom-right!")
elif victoryFlag == 6:
    print("You won by top-left to bottom-right!")
elif victoryFlag == 7:
    print("The CPU wins by bottom-left to top-right!")
elif victoryFlag == 8:
    print("You won by bottom-left to top-right!")
else:
    print("It was a draw!")

input("")
