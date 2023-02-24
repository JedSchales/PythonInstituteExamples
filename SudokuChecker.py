'''
This program is designed to take row-by-row input from a user to create a standard 9 x 9 Sudoku board and validate its solution.
'''


def testRows(board):                            #Define a function to test the validity of each row in a given board
    for rows in range(9):
        testRow = "".join(str(board[rows][:]))  #Construct a string that contains each digit within one row of the board
        for z in range(1,10):                   #Iterate through the digits 1-9, searching for one instance of each number
            validRow = testRow.find(str(z))
            if validRow == -1:                  #Flag an invalid row and return "False"
                print("A ", z, " was not found in row ", rows+1, sep="")
                return 0
    return 1
    
def testCols(board):                            #Define a function to test the validity of each column in a given board
    for cols in range(9):
        testCol = ''
        for elem in range(9):
            testCol += str(board[elem][cols])   #Construct a string that contains each digit within one column of the board
        for z in range(1,10):                   #Iterate through the digits 1-9, searching for one instance of each number
            validCol = testCol.find(str(z))
            if validCol == -1:                  #Flag an invalid column and return "False"
                print("A ", z, " was not found in column ", cols+1, sep="")
                return 0
    return 1
    
def testTiles(board):                           #Define a function to test the validity of each 3x3 sub-square or "tile" in a given board
    tileNum = 1                                 #Create a tile numbering scheme for debugging and reporting to end user
    testTile = ''
    for rowStart in range(0,9,3):
        for colStart in range(0,9,3):
            for rows in range(rowStart,rowStart+3):
                for cols in range(colStart,colStart+3):
                    testTile += str(board[rows][cols])  #Construct a string that contains each digit within one 3x3 sub-square of the board
            for z in range(1,10):                       #Iterate through the digits 1-9, searching for one instance of each number
                validTile = testTile.find(str(z))
                if validTile == -1:                     #Flag an invalid sub-square and return "False"
                    print("A ", z, " was not found in tile ", tileNum, sep="")
                    return 0
            tileNum += 1
            testTile = ''                               #Re-initialize the testTile string for the next loop iteration
    return 1

        
board = [[0 for i in range(9)] for j in range(9)]       #Initialize a blank Sudoku board.

#Pass through a pre-filled, valid Sudoku board for debugging
#board = [[2,9,5,7,4,3,8,6,1],[4,3,1,8,6,5,9,2,7],[8,7,6,1,9,2,5,4,3],[3,8,7,4,5,9,2,1,6],[6,1,2,3,8,7,4,9,5],[5,4,9,2,1,6,7,3,8],[7,6,3,5,2,4,1,8,9],[9,2,8,6,7,1,3,5,4],[1,5,4,9,3,8,6,7,2]]

validNum = 0                                            #Initialize a variable used to validate input data

for i in range(9):
    while board[i][0] == 0:                             #If no board is passed in, prompt user for each of the 9 rows
        try:                                            #Catch non-numeric input data
            promptText = ("Please enter row", str(i+1), "of the Sudoku puzzle as a 9-digit integer: ")
            validNum = int(input(" ".join(promptText)))
            if len(str(validNum)) != 9:                 #Catch input data that does not contain exactly 9 digits.
                print("The input should be a 9-digit integer.  Please try again.")
            else:
                rowstring = str(validNum)
                for j in range(9):
                    board[i][j] = rowstring[j]          #Fill the specified row in the empty board with the user's data
        except:
            print("The provided input contained non-numeric characters.  Please try again.")

flag1 = testRows(board)                         #Run the testRows function on the board to determine validity of the row rule.
if flag1 != 0:
    print("All rows are legal.")
else:
    print("Rows are not legal.")

flag2 = testCols(board)                         #Run the testCols function on the board to determine validity of the column rule.
if flag2 != 0:
    print("All columns are legal.")
else:
    print("Columns are not legal.")
    
flag3 = testTiles(board)                        #Run the testTiles function on the board to determine validity of the sub-square rule.
if flag3 != 0:
    print("All sub-squares are legal.")
else:
    print("Sub-squares are not legal.")
