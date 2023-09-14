from piece import Piece


class GameLogic:
    print("Game Logic Object Created")

    # TODO add code here to manage the logic of your game
    def __init__(self, boardArray):
        self.turn = Piece.White
        self.boardArray = boardArray
        self.xPos = 0
        self.yPos = 0
        self.blackPrisoners = 0
        self.whitePrisoners = 0

    def setCurrentPosition(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    # def isSlotVacant(self):
    #     return self.boardArray[self.yPos][self.xPos].Piece == Piece.NoPiece

    def isSlotVacant(self, boardArray, x, y):
        return boardArray[y][x].Status == Piece.NoPiece

    def validateMove(self, boardArray, x, y):
        return self.isSlotVacant(boardArray, x, y)

    def updateLiberties(self, boardArray):
        for row in boardArray:
            for cell in row:
                liberties = 0
                piece = cell.Status
                if piece != Piece.NoPiece:
                    liberties += cell.computeLiberties(boardArray, piece)
                    print("x=", str(cell.x), "; y=", str(cell.y), "; liberties: ", str(liberties))

    def isIllegalMove(self):
        pass

    def placePiece(self, boardArray, x, y):
        nextTurn = self.getNextTurn()
        boardArray[y][x].Status = nextTurn

    def getNextTurn(self):
        nextTurn = self.turn
        if nextTurn == Piece.Black:
            nextTurn = Piece.White
        else:
            nextTurn = Piece.Black
        self.turn = nextTurn
        return nextTurn

    # capturing
    def initCapturing(self, boardArray, xPos, yPos):
        piece = boardArray[yPos][xPos]
        upPiece = piece.getUp(boardArray)
        downPiece = piece.getDown(boardArray)
        rightPiece = piece.getRight(boardArray)
        leftPiece = piece.getLeft(boardArray)

        if upPiece is not None and upPiece.liberties == 0 and upPiece.Status is not Piece.NoPiece:
            return self.capturePiece(boardArray, upPiece)

        elif downPiece is not None and downPiece.liberties == 0 and downPiece.Status is not Piece.NoPiece:
            return self.capturePiece(boardArray, downPiece)

        elif rightPiece is not None and rightPiece.liberties == 0 and rightPiece.Status is not Piece.NoPiece:
            return self.capturePiece(boardArray, rightPiece)

        elif leftPiece is not None and leftPiece.liberties == 0 and leftPiece.Status is not Piece.NoPiece:
            return self.capturePiece(boardArray, leftPiece)

    # capture piece
    def capturePiece(self, boardArray, piece):
        # captures a piece at the given position
        xPos = piece.x
        yPos = piece.y

        if boardArray[yPos][xPos].Status == Piece.White:  # if the piece is white
            self.blackPrisoners += 1
            self.boardArray[yPos][xPos] = Piece(Piece.NoPiece, xPos, yPos)
            return "White Stone Captured at x: " + str(xPos) + ", y: " + str(yPos)

        else:  # if the piece is black
            self.whitePrisoners += 1
            boardArray[yPos][xPos] = Piece(Piece.NoPiece, xPos, yPos)
            return "Black Stone Captured at x: " + str(xPos) + ", y: " + str(yPos)

    # def capturePiece(self, boardArray, xPos, yPos):
    #     # captures a piece at the given position
    #     if boardArray[yPos][xPos].Piece == Piece.White:  # if the piece is white
    #         self.blackPrisoners += 1
    #         self.boardArray[yPos][xPos] = Piece(Piece.NoPiece, xPos, yPos)
    #         return "White Stone Captured at x: " + str(xPos) + ", y: " + str(yPos)
    #
    #     else:  # if the piece is black
    #         self.whitePrisoners += 1
    #         boardArray[yPos][xPos] = Piece(Piece.NoPiece, xPos, yPos)
    #         return "Black Stone Captured at x: " + str(xPos) + ", y: " + str(yPos)


