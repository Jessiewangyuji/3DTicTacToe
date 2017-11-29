def displayBoard():
    global board
    for i in range(4):
        print "\nLevel", i
        level = board[i]
        for j in range(4):
            for k in range(4):
                print level[j][k],
            print

def checkWin():
    if checkHorizontal():
        if count % 2 == 1:
            print 'X has won the game'
        else:
            print 'O has won the game'
        return True
    elif checkVertical():
        if count % 2 == 1:
            print 'X has won the game'
        else:
            print 'O has won the game'
        return True
    elif checkDiagonal():
        if count % 2 == 1:
            print 'X has won the game'
        else:
            print 'O has won the game'
        return True
    return False

def checkHorizontal():
    global board
    for i in range(4):
        level = board[i]
        for j in range(4):
            if level[j][0] != '_' and level[j][0] == level[j][1] and \
                level[j][1] == level[j][2] and level[j][2] == level[j][3]:
                return True
            if level[0][j] != '_' and level[0][j] == level[1][j] and \
                level[1][j] == level[2][j] and level[2][j] == level[3][j]:
                return True
        if level[0][0] != '_' and level[0][0] == level[1][1] and \
            level[1][1] == level[2][2] and level[2][2] == level[3][3]:
            return True
        if level[0][3] != '_' and level[0][3] == level[1][2] and \
            level[1][2] == level[2][1] and level[2][1] == level[3][0]:
            return True
    return False

def checkVertical():
    global board
    for k in range(4):
        for j in range(4):
            if board[0][j][k] != '_' and board[0][j][k] == board[1][j][k] and \
                board[1][j][k] == board[2][j][k] and board[2][j][k] == board[3][j][k]:
                return True
        if board[0][0][k] != '_' and board[0][0][k] == board[1][1][k] and \
            board[1][1][k] == board[2][2][k] and board[2][2][k] == board[3][3][k]:
            return True
        if board[0][k][0] != '_' and board[0][k][0] == board[1][k][1] and \
            board[1][k][1] == board[2][k][2] and board[2][k][2] == board[3][k][3]:
            return True
    return False

def checkDiagonal():
    global board
    if board[0][0][0] != '_' and board[0][0][0] == board[1][1][1] and \
        board[1][1][1] == board[2][2][2] and board[2][2][2] == board[3][3][3]:
        return True
    if board[0][0][3] != '_' and board[0][0][3] == board[1][1][2] and \
        board[1][1][2] == board[2][2][1] and board[2][2][1] == board[3][3][0]:
        return True
    if board[0][3][0] != '_' and board[0][3][0] == board[1][2][1] and \
        board[1][2][1] == board[2][1][2] and board[2][1][2] == board[3][0][3]:
        return True
    if board[0][3][3] != '_' and board[0][3][3] == board[1][2][2] and \
        board[1][2][2] == board[2][1][1] and board[2][1][1] == board[3][0][0]:
        return True
    return False

def getInput():
    global count
    global board

    while True:
        input = raw_input("Which cell do you want to place your move? (level, x, y)")
        level, x, y = input.split(' ')
        level = int(level)
        x = int(x)
        y = int(y)

        if level < 0 or level >= 4 or x < 0 or x >= 4 or y < 0 or y >= 4:
            print "Invalid cell location"
        elif board[level][x][y] != '_':
            print "Cell is not available to place your move. Please choose an empty cell"
        else:
            board[level][x][y] = 'X' if count % 2 == 0 else 'O'
            break
    count += 1
    displayBoard()

def heuristic(level1, x1, y1, level2, x2, y2):
    if board[level1][x1][y1] != '_' or board[level2][x2][y2] != '_':
        return -float("inf")
    myMove = 'X' if count % 2 == 0 else 'O'
    opponentMove = 'O' if count % 2 == 0 else 'X'
    board[level1][x1][y1] = 'X' if count % 2 == 0 else 'O'
    board[level2][x2][y2] = 'O' if count % 2 == 0 else 'X'
#displayBoard()
    eval = 0
    #horizontal
    myCount = 0
    opponentCount = 0
    for i in range(4):
        if board[level1][x1][i] == myMove:
            myCount += 1
        elif board[level1][x1][i] == opponentMove:
            opponentCount += 1
    eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    for i in range(4):
        if board[level1][i][y1] == myMove:
            myCount += 1
        elif board[level1][i][y1] == opponentMove:
            opponentCount += 1
    eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (x1 - y1) == 0:
        for i in range(4):
            if board[level1][i][i] == myMove:
                myCount += 1
            elif board[level1][i][i] == opponentCount:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if x1 + y1 == 3:
        for i in range(4):
            if board[level1][i][3 - i] == myMove:
                myCount += 1
            elif board[level1][i][3 - i] == opponentCount:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)

    board[level1][x1][y1] = '_'
    board[level2][x2][y2] = '_'

    #vertical
    myCount = 0
    opponentCount = 0
    for i in range(4):
        if board[i][x1][y1] == myMove:
            myCount += 1
        elif board[i][x1][y1] == opponentMove:
            opponentCount += 1
    eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (level1 - x1) == 0:
        for i in range(4):
            if board[i][i][y1] == myMove:
                myCount += 1
            elif board[i][i][y1] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (level1 + x1) == 3:
        for i in range(4):
            if board[i][3 - i][y1] == myMove:
                myCount += 1
            elif board[i][3 - i][y1] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (level1 - y1) == 0:
        for i in range(4):
            if board[i][x1][i] == myMove:
                myCount += 1
            elif board[i][x1][i] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (level1 + y1) == 3:
        for i in range(4):
            if board[i][x1][3 - i] == myMove:
                myCount += 1
            elif board[i][x1][3 - i] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)

    #diagonal
    myCount = 0
    opponentCount = 0
    if level1 == x1 and x1 == y1:
        for i in range(4):
            if board[i][i][i] == myMove:
                myCount += 1
            elif board[i][i][i] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (level1 == x1) and (y1 == (3 - level1)):
        for i in range(4):
            if board[i][i][3 - i] == myMove:
                myCount += 1
            elif board[i][i][3 - i] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (level1 == y1) and (x1 == (3 - level1)):
        for i in range(4):
            if board[i][3 - i][i] == myMove:
                myCount += 1
            elif board[i][3 - i][i] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    myCount = 0
    opponentCount = 0
    if (x1 == y1) and (x1 == (3 - level1)):
        for i in range(4):
            if board[3 - i][i][i] == myMove:
                myCount += 1
            elif board[3 - i][i][i] == opponentMove:
                opponentCount += 1
        eval += 0 if opponentCount > 0 else pow(76, myCount - 1)
    return eval

def minmax():
    dict = {}
    for i1 in range(4):
        for j1 in range(4):
            for k1 in range(4):
                loc = str(i1) + str(j1) + str(k1)
                for i2 in range(4):
                    for j2 in range(4):
                        for k2 in range(4):
                            val = heuristic(i1, j1, k1, i2, j2, k2)
                            print(val, loc in dict)
                            if val == -float("inf"):
                                continue
                            if loc in dict:
                                dict[loc] = min(val, dict[loc])
                            else:
                                dict[loc] = val
                            #dict[loc] = val if loc not in dict else min(val, dict[loc])
    currMax = -float("inf")
    currLoc = ""
    print(dict)
    for loc in dict:
        if currMax > dict[loc]:
            continue
        else:
            currMax = dict[loc]
            currLoc = loc
    return currMax, loc

count = 0
board = [[['_' for k in range(4)] for j in range(4)] for i in range(4)]
#board[0][0][0] = 'X'
#board[0][0][1] = 'X'
#board[0][2][2] = 'O'
#print(minmax())
#heuristic(0, 0, 2, 1, 1, 1)
while True:
    displayBoard()
    getInput()
    if checkWin():
        break
    currMax, loc = minmax()
    board[int(loc[0])][int(loc[1])][int(loc[2])] = 'O'
    count += 1
