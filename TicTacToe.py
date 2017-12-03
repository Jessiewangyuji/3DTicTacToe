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
#displayBoard()

def heuristic(player):
    global board
    myMove = 'X' if player % 2 == 0 else 'O'
    opponentMove = 'O' if player % 2 == 0 else 'X'
    #board[level1][x1][y1] = 'X' if count % 2 == 0 else 'O'
    #board[level2][x2][y2] = 'O' if count % 2 == 0 else 'X'
    #displayBoard()
    eval = 0
    #horizontal
    myCount = 0
    opponentCount = 0
    for i in range(4):
        levelBoard = board[i]
        #horizontal
        for j in range(4):
            myPrev = 0
            myCount = 0
            opponentCount = 0
            for k in range(4):
                if levelBoard[j][k] == opponentMove:
                    opponentCount += 1
                    break
                elif levelBoard[j][k] == '_':
                    myPrev = 0
                else:
                    myPrev += 1 if k == 0 or levelBoard[j][k - 1] == levelBoard[j][k] else 1
                    myCount = max(myPrev, myCount)
            eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
        #vertical
        for k in range(4):
            myPrev = 0
            myCount = 0
            opponentCount = 0
            for j in range(4):
                if levelBoard[j][k] == opponentMove:
                    opponentCount += 1
                    break
                elif levelBoard[j][k] == '_':
                    myPrev = 0
                else:
                    myPrev += 1 if j == 0 or levelBoard[j - 1][k] == levelBoard[j][k] else 1
                    myCount = max(myPrev, myCount)
            eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
            
        myPrev = 0
        myCount = 0
        opponentCount = 0
        for j in range(4):
            if levelBoard[j][j] == opponentMove:
                opponentCount += 1
                break
            elif levelBoard[j][j] == '_':
                myPrev = 0
            else:
                myPrev += 1 if j == 0 or levelBoard[j - 1][j - 1] == levelBoard[j][j] else 1
                myCount = max(myPrev, myCount)
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

        myPrev = 0
        myCount = 0
        opponentCount = 0
        for j in range(4):
            if levelBoard[j][3 - j] == opponentMove:
                opponentCount += 1
                break
            elif levelBoard[j][3 - j] == '_':
                myPrev = 0
            else:
                myPrev += 1 if j == 0 or levelBoard[j - 1][3 - (j - 1)] == levelBoard[j][3 - j] else 1
                myCount = max(myPrev, myCount)
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
            
    #vertical
    for j in range(4):
        for k in range(4):
            myCount = 0
            opponentCount = 0
            myPrev = 0
            for i in range(4):
                if board[i][j][k] == opponentMove:
                    opponentCount += 1
                    break
                elif board[i][j][k] == '_':
                    myPrev = 0
                else:
                    myPrev += 1 if i == 0 or board[i - 1][j][k] == board[i][j][k] else 1
                    myCount = max(myPrev, myCount)
            eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    for j in range(4):
        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][j][i] == opponentMove:
                opponentCount += 1
                break
            elif board[i][j][i] == '_':
                myPrev = 0
            else:
                myPrev += 1 if i == 0 or board[i - 1][j][i - 1] == board[i][j][i] else 1
                myCount = max(myPrev, myCount)
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][j][3 - i] == opponentMove:
                opponentCount += 1
                break
            elif board[i][j][3 - i] == '_':
                myPrev = 0
            else:
                myPrev += 1 if i == 0 or board[i - 1][j][3 - (i - 1)] == board[i][j][3 - i] else 1
                myCount = max(myPrev, myCount)
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][i][j] == opponentMove:
                opponentCount += 1
                break
            elif board[i][i][j] == '_':
                myPrev = 0
            else:
                myPrev += 1 if i == 0 or board[i - 1][i - 1][j] == board[i][i][j] else 1
                myCount = max(myPrev, myCount)
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][3 - i][j] == opponentMove:
                opponentCount += 1
                break
            elif board[i][3 - i][j] == '_':
                myPrev = 0
            else:
                myPrev += 1 if i == 0 or board[i - 1][3 - (i - 1)][j] == board[i][3 - i][j] else 1
                myCount = max(myPrev, myCount)
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    #diagonal
    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[i][i][i] == opponentMove:
            opponentCount += 1
            break
        elif board[i][i][i] == '_':
            myPrev = 0
        else:
            myPrev += 1 if i == 0 or board[i - 1][i - 1][i - 1] == board[i][i][i] else 1
            myCount = max(myPrev, myCount)
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[i][i][3 - i] == opponentMove:
            opponentCount += 1
            break
        elif board[i][i][3 - i] == '_':
            myPrev = 0
        else:
            myPrev += 1 if i == 0 or board[i - 1][i - 1][3 - (i - 1)] == board[i][i][3 - i] else 1
            myCount = max(myPrev, myCount)
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[i][3 - i][i] == opponentMove:
            opponentCount += 1
            break
        elif board[i][3 - i][i] == '_':
            myPrev = 0
        else:
            myPrev += 1 if i == 0 or board[i - 1][3 - (i - 1)][i - 1] == board[i][3 - i][i] else 1
            myCount = max(myPrev, myCount)
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[3 - i][i][i] == opponentMove:
            opponentCount += 1
            break
        elif board[3 - i][i][i] == '_':
            myPrev = 0
        else:
            myPrev += 1 if i == 0 or board[3 - (i - 1)][i - 1][i - 1] == board[3 - i][i][i] else 1
            myCount = max(myPrev, myCount)
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    return eval

def minmax():
    max_dict = {}
    min_dict = {}
    for i1 in range(4):
        for j1 in range(4):
            for k1 in range(4):
                if board[i1][j1][k1] != '_':
                    continue
                else:
                    board[i1][j1][k1] = 'X' if count % 2 == 0 else 'O'
                loc = str(i1) + str(j1) + str(k1)
                currMax = -float("inf")
                oppoMin = float("inf")
                for i2 in range(4):
                    for j2 in range(4):
                        for k2 in range(4):
                            myVal = heuristic(count)

                            if board[i2][j2][k2] != '_':
                                continue
                            else:
                                board[i2][j2][k2] = 'O' if count % 2 == 0 else 'X'

                            oppoVal = heuristic(count + 1)

#print myVal, oppoVal
                            currMax = max(currMax, myVal)
                            oppoMin = min(oppoMin, oppoVal)
                            board[i2][j2][k2] = '_'
                
                max_dict[loc] = currMax
                min_dict[loc] = oppoMin
                board[i1][j1][k1] = '_'

    minVal = float("inf")

#print min_dict
#print max_dict
    
    for loc in min_dict:
        if minVal <= min_dict[loc]:
            continue
        else:
            minVal = min_dict[loc]
#print minVal

    maxLoc = ""
    maxVal = -float("inf")
    for loc in min_dict:
        if min_dict[loc] == minVal:
            if maxVal >= max_dict[loc]:
                continue
            else:
                maxVal = max_dict[loc]
                maxLoc = loc
    return maxVal, maxLoc

count = 0
board = [[['_' for k in range(4)] for j in range(4)] for i in range(4)]
#board[0][0][0] = 'X'
#board[0][0][1] = 'X'
#board[0][0][2] = 'X'
#board[2][1][2] = 'O'
#board[2][3][0] = 'O'
#board[0][0][3] = 'O'

#print(minmax())
#print(heuristic(1))
#print(heuristic(2, 2, 2, 0, 0, 2, 0))

while True:
    displayBoard()
    getInput()
    if checkWin():
        break

    currMax, loc = minmax()
    board[int(loc[0])][int(loc[1])][int(loc[2])] = 'O'
    if checkWin():
        break
    count += 1
