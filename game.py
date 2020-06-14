import time

# Variables
amountOfPlayers = 2
currentTurnOrder_PlayerNumber = 1
inputSize = 3
boardSize = int(inputSize ** 2)
gameBoard = []
gameIsRunning = True


def SetupBoard():
    # Setups up the array
    for i in range(boardSize):
        gameBoard.insert(i, str(i + 1))


def DrawBoard():
    # Displays the board to the console
    for i in range(10):
        print("\n")
    counter = 0
    rowToPrint = ""
    for i in range(boardSize):
        rowToPrint += gameBoard[i]
        counter += 1
        if counter <= inputSize - 1:
            rowToPrint += " | "
        elif counter >= inputSize:
            print(rowToPrint)
            rowToPrint = ""
            counter = 0
    print("\n")


def ValidTurn(turnPosition: int):
    if turnPosition >= 0 and turnPosition <= len(gameBoard):
        if gameBoard[turnPosition] != "X" and gameBoard[turnPosition] != "⦿":
            return True
        else:
            return False


def GetPlayerTag():
    global currentTurnOrder_PlayerNumber
    if currentTurnOrder_PlayerNumber == 1:
        return "Player X"
    else:
        return "Player ⦿"


def GameOver(victoryMessage):
    global gameIsRunning
    print(victoryMessage)
    time.sleep(3)
    gameIsRunning = True
    Game()


def CheckRows():
    global gameIsRunning

    row1 = gameBoard[0] == gameBoard[1] == gameBoard[2]
    row2 = gameBoard[3] == gameBoard[4] == gameBoard[5]
    row3 = gameBoard[6] == gameBoard[7] == gameBoard[8]

    if row1 or row2 or row3:
        gameIsRunning = False
        GameOver(GetPlayerTag() + " has won the game by three in a row!!!")
    return


def CheckColumns():
    global gameIsRunning

    column1 = gameBoard[0] == gameBoard[3] == gameBoard[6]
    column2 = gameBoard[1] == gameBoard[4] == gameBoard[7]
    column3 = gameBoard[2] == gameBoard[5] == gameBoard[8]

    if column1 or column2 or column3:
        gameIsRunning = False
        GameOver(GetPlayerTag() + " has won the game by three in a row!!!")
    return


def CheckDiagonals():
    global gameIsRunning

    diagonal1 = gameBoard[0] == gameBoard[4] == gameBoard[8]
    diagonal2 = gameBoard[2] == gameBoard[4] == gameBoard[6]

    if diagonal1 or diagonal2:
        gameIsRunning = False
        GameOver(GetPlayerTag() + " has won the game by three in a row!!!")
    return


def CheckForWin():
    CheckRows()
    CheckColumns()
    CheckDiagonals()


def CheckForTie():
    for i in range(boardSize):
        boardValue = gameBoard[i]
        if str.isdigit(boardValue):
            return False

    return True


def CheckGameStatus():
    # Checks the current game moves and determines if there is a win/lose or tie
    CheckForWin()
    CheckForTie()


def ChangePlayerTurn():
    global currentTurnOrder_PlayerNumber
    currentTurnOrder_PlayerNumber += 1
    if currentTurnOrder_PlayerNumber > amountOfPlayers:
        currentTurnOrder_PlayerNumber = 1


def HandleTurns():
    # Makes a turn on the board by getting input from the player and then displaying it
    print(GetPlayerTag() + "'s turn")
    selectedPosition = None
    while (
        selectedPosition == None or selectedPosition > boardSize or selectedPosition < 0
    ):
        userPosition = input(
            "Select a position to change ("
            + str(boardSize - boardSize + 1)
            + "-"
            + str(boardSize)
            + "): "
        )
        if ValidTurn(int(userPosition) - 1):
            selectedPosition = int(userPosition) - 1
        else:
            print("You cannot make that turn!")

    if currentTurnOrder_PlayerNumber == 1:
        gameBoard[selectedPosition] = "X"
    else:
        gameBoard[selectedPosition] = "⦿"

    DrawBoard()
    CheckGameStatus()
    ChangePlayerTurn()


def Game():
    SetupBoard()
    DrawBoard()
    while gameIsRunning:
        HandleTurns()


# Starts the game
Game()
