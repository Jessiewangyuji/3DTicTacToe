import random
from sets import Set

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
    global numHand
    if checkHorizontal():
        if count % 2 == 1:
            print 'X has won the game in %d steps' % numHand
        else:
            print 'O has won the game in %d steps' % numHand
        return True
    elif checkVertical():
        if count % 2 == 1:
            print 'X has won the game in %d steps' % numHand
        else:
            print 'O has won the game in %d steps' % numHand
        return True
    elif checkDiagonal():
        if count % 2 == 1:
            print 'X has won the game in %d steps' % numHand
        else:
            print 'O has won the game in %d steps' % numHand
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
        if board[0][3][k] != '_' and board[0][3][k] == board[1][2][k] and \
            board[1][2][k] != board[2][1][k] and board[2][1][k] == board[3][0][k]:
            return True
        if board[0][k][0] != '_' and board[0][k][0] == board[1][k][1] and \
            board[1][k][1] == board[2][k][2] and board[2][k][2] == board[3][k][3]:
            return True
        if board[0][k][3] != '_' and board[0][k][3] == board[1][k][2] and \
            board[1][k][2] == board[2][k][1] and board[2][k][1] == board[3][k][0]:
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
        level, x, y = input.strip().split(' ')
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
                    continue
                else:
                    myCount += 1
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
                    continue
                else:
                    myCount += 1
            eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
            
        myCount = 0
        opponentCount = 0
        for j in range(4):
            if levelBoard[j][j] == opponentMove:
                opponentCount += 1
                break
            elif levelBoard[j][j] == '_':
                continue
            else:
                myCount += 1
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

        myCount = 0
        opponentCount = 0
        for j in range(4):
            if levelBoard[j][3 - j] == opponentMove:
                opponentCount += 1
                break
            elif levelBoard[j][3 - j] == '_':
                continue
            else:
                myCount += 1
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
                    continue
                else:
                    myCount += 1
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
                continue
            else:
                myCount += 1
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][j][3 - i] == opponentMove:
                opponentCount += 1
                break
            elif board[i][j][3 - i] == '_':
                continue
            else:
                myCount += 1
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][i][j] == opponentMove:
                opponentCount += 1
                break
            elif board[i][i][j] == '_':
                continue
            else:
                myCount += 1
        eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))
        myCount = 0
        opponentCount = 0
        myPrev = 0
        for i in range(4):
            if board[i][3 - i][j] == opponentMove:
                opponentCount += 1
                break
            elif board[i][3 - i][j] == '_':
                continue
            else:
                myCount += 1
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
            continue
        else:
            myCount += 1
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[i][i][3 - i] == opponentMove:
            opponentCount += 1
            break
        elif board[i][i][3 - i] == '_':
            continue
        else:
            myCount += 1
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[i][3 - i][i] == opponentMove:
            opponentCount += 1
            break
        elif board[i][3 - i][i] == '_':
            continue
        else:
            myCount += 1
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    myCount = 0
    opponentCount = 0
    myPrev = 0
    for i in range(4):
        if board[3 - i][i][i] == opponentMove:
            opponentCount += 1
            break
        elif board[3 - i][i][i] == '_':
            continue
        else:
            myCount += 1
    eval += 0 if opponentCount > 0 else int(pow(76, myCount - 1))

    return eval

def minmax():
    max_dict = {}
    min_dict = {}
    prune = Set()
    loc = ""
    beta = float("inf")
    
    for i1 in range(4):
        for j1 in range(4):
            for k1 in range(4):
                if board[i1][j1][k1] != '_':
                    continue
                else:
                    board[i1][j1][k1] = 'X' if count % 2 == 0 else 'O'
                loc = str(i1) + str(j1) + str(k1)
                myVal = heuristic(count)
                if myVal >= int(pow(76, 3)):
                    return myVal, loc
            #currMax = -float("inf")
                oppoMax = -float("inf")
                for i2 in range(4):
                    for j2 in range(4):
                        for k2 in range(4):
                            loc2 = str(i2) + str(j2) + str(k2)
                            #if loc2 in prune:
                            #    continue
                            
                            if board[i2][j2][k2] != '_':
                                continue
                            else:
                                board[i2][j2][k2] = 'O' if count % 2 == 0 else 'X'

                            oppoVal = heuristic(count + 1)

#currMax = max(currMax, myVal)
#print(currMax)
                            oppoMax = max(oppoMax, oppoVal)
                            if oppoVal <= beta:
                                beta = oppoMax
                            else: #Can prune opponent move
                                prune.add(loc2)
                            
                            board[i2][j2][k2] = '_'
                
                max_dict[loc] = myVal
                min_dict[loc] = oppoMax
                board[i1][j1][k1] = '_'

    print prune
    print min_dict
    minVal = float("inf")
    
    for loc in min_dict:
        if minVal <= min_dict[loc]:
            continue
        else:
            minVal = min_dict[loc]

    maxLoc = ""
    maxVal = -float("inf")
    for loc in min_dict:
        if min_dict[loc] == minVal:
            if maxVal >= max_dict[loc]:
                continue
            else:
                maxVal = max_dict[loc]
                maxLoc = loc
    return maxVal, maxLoc or loc

count = 0
board = [[['_' for k in range(4)] for j in range(4)] for i in range(4)]

numHand = 0
while True:
    if numHand == 32:
        print "DRAW!"
        break
    displayBoard()
    getInput()
    numHand += 1
    if checkWin():
        displayBoard()
        break

    currMax, loc = minmax()
    board[int(loc[0])][int(loc[1])][int(loc[2])] = 'X' if count % 2 == 0 else 'O'

    count += 1
    if checkWin():
        displayBoard()
        break
