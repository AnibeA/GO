# TODO: Add more functions as needed for your Pieces

MAX_WIDTH = 7
MAX_HEIGHT = 7


class Piece(object):
    NoPiece = 0
    White = 1
    Black = 2
    Status = 0 #default to nopiece
    liberties = 0 #default no liberties
    x = -1
    y = -1

    def __init__(self, Piece, x, y):  #constructor
        self.Status = Piece
        self.liberties = 0
        self.x = x
        self.y = y

    def getPiece(self): # return PieceType
        return self.Status

    def getLiberties(self): # return Liberties
        return self.liberties

    def setLiberties(self, liberties): # set Liberties
        self.liberties = liberties

    # get piece vertically upward
    def getUp(self, boardArray):
        if self.y == 0:
            return None
        else:
            return boardArray[self.y-1][self.x]  # move y coordinate upwards

    # get piece vertically download
    def getDown(self, boardArray):
        if self.y == MAX_WIDTH - 1:
            return None
        else:
            return boardArray[self.y + 1][self.x]  # move y coordinate to downwards

    def getLeft(self, boardArray):
        if self.x == 0:
            return None
        else:
            return boardArray[self.y][self.x-1]  # move x coordinate to the left

    def getRight(self, boardArray):
        if self.x == MAX_HEIGHT - 1:
            return None
        else:
            return boardArray[self.y][self.x+1]  # move x coordinate to the right

    def getUpLiberty(self, boardArray, current):
        return self.__computeLiberties(self.getUp(boardArray), current)

    def getDownLiberty(self, boardArray, current):
        return self.__computeLiberties(self.getDown(boardArray), current)

    def getRightLiberty(self, boardArray, current):
        return self.__computeLiberties(self.getRight(boardArray), current)

    def getLeftLiberty(self, boardArray, current):
        return self.__computeLiberties(self.getLeft(boardArray), current)

    def computeLiberties(self, boardArray, piece):
        liberties = 0
        liberties += self.getUpLiberty(boardArray, piece)
        liberties += self.getDownLiberty(boardArray, piece)
        liberties += self.getRightLiberty(boardArray, piece)
        liberties += self.getLeftLiberty(boardArray, piece)
        self.setLiberties(liberties)
        return liberties

    @staticmethod
    def __computeLiberties(piece, current):
        if piece is None:
            return 0
        elif piece.Status == Piece.NoPiece or piece.Status == current:
            return 1
        else:
            return 0

