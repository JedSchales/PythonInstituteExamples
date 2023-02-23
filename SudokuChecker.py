def testRows(board):
    for rows in range(9):
        testRow = "".join(str(board[rows][:]))
        for z in range(1,10):
            validRow = testRow.find(str(z))
            if validRow == -1:
                print("A ", z, " was not found in row ", rows+1, sep="")
                return 0
    return 1
    
def testCols(board):
    for cols in range(9):
        testCol = ''
        for elem in range(9):
            testCol += str(board[elem][cols])
        for z in range(1,10):
            validCol = testCol.find(str(z))
            if validCol == -1:
                print("A ", z, " was not found in column ", cols+1, sep="")
                return 0
    return 1
    
def testTiles(board):
    tileNum = 1
    testTile = ''
    for rowStart in range(0,9,3):
        for colStart in range(0,9,3):
            for rows in range(rowStart,rowStart+3):
                for cols in range(colStart,colStart+3):
                    testTile += str(board[rows][cols])
            for z in range(1,10):
                validTile = testTile.find(str(z))
                if validTile == -1:
                    print("A ", z, " was not found in tile ", tileNum, sep="")
                    return 0
            tileNum += 1
            testTile = ''
    return 1
            
    for cols in range(9):
        testCol = ''
        for elem in range(9):
            testCol += str(board[elem][cols])
        for z in range(1,10):
            validCol = testCol.find(str(z))
            if validCol == -1:
                print("A ", z, " was not found in column ", cols+1, sep="")
                return 0
    return 1
        
board = [[0 for i in range(9)] for j in range(9)]
#board = [[2,9,5,7,4,3,8,6,1],[4,3,1,8,6,5,9,2,7],[8,7,6,1,9,2,5,4,3],[3,8,7,4,5,9,2,1,6],[6,1,2,3,8,7,4,9,5],[5,4,9,2,1,6,7,3,8],[7,6,3,5,2,4,1,8,9],[9,2,8,6,7,1,3,5,4],[1,5,4,9,3,8,6,7,2]]

validNum = 0

for i in range(9):
    while board[i][0] == 0:
        try:
            promptText = ("Please enter row", str(i+1), "of the Sudoku puzzle as a 9-digit integer: ")
            validNum = int(input(" ".join(promptText)))
            if len(str(validNum)) != 9:
                print("The input should be a 9-digit integer.  Please try again.")
            else:
                rowstring = str(validNum)
                for j in range(9):
                    board[i][j] = rowstring[j]
        except:
            print("The provided input contained non-numeric characters.  Please try again.")

flag1 = testRows(board)
if flag1 != 0:
    print("All rows are legal.")
else:
    print("Rows are not legal.")

flag2 = testCols(board)
if flag2 != 0:
    print("All columns are legal.")
else:
    print("Columns are not legal.")
    
flag3 = testTiles(board)
if flag3 != 0:
    print("All sub-squares are legal.")
else:
    print("Sub-squares are not legal.")
