import self
from PyQt6.QtWidgets import QDockWidget, QVBoxLayout, QWidget, QLabel, \
    QFrame  # TODO import additional Widget classes as desired
from PyQt6.QtCore import pyqtSlot

from piece import Piece


class ScoreBoard(QDockWidget):
    '''# base the score_board on a QDockWidget'''

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        '''initiates ScoreBoard UI'''
        self.resize(200, 200)
        self.center()
        self.setWindowTitle('ScoreBoard')
        #create a widget to hold other widgets
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()

        #create two labels which will be updated by signals
        self.instructions = QLabel("Instructions:")
        self.currTurn = QLabel("Current Turn:")




        self.label_clickLocation = QLabel("Click Location: ")
        self.label_timeRemaining = QLabel("Time remaining: ")

        self.mainWidget.setLayout(self.mainLayout)

        self.mainLayout.addWidget(self.instructions)
        self.mainLayout.addWidget(self.currTurn)


        self.mainLayout.addWidget(self.label_clickLocation)
        self.mainLayout.addWidget(self.label_timeRemaining)
        self.setWidget(self.mainWidget)
        self.show()

    def center(self):
        '''centers the window on the screen, you do not need to implement this method'''

    def make_connection(self, board):
        '''this handles a signal sent from the board class'''
        # when the clickLocationSignal is emitted in board the setClickLocation slot receives it
        board.clickLocationSignal.connect(self.setClickLocation)
        # when the updateTimerSignal is emitted in the board the setTimeRemaining slot receives it
        board.updateTimerSignal.connect(self.setTimeRemaining)
        # when the turns change, the colours change


    @pyqtSlot(str) # checks to make sure that the following slot is receiving an argument of the type 'int'
    def setClickLocation(self, clickLoc):
        '''updates the label to show the click location'''
        self.label_clickLocation.setText("Click Location:" + clickLoc)
        print('slot ' + clickLoc)

    @pyqtSlot(int)
    def setTimeRemaining(self, timeRemainng):
        '''updates the time remaining label to show the time remaining'''
        update = "Time Remaining:" + str(timeRemainng)
        self.label_timeRemaining.setText(update)
        print('slot '+update)
        # self.redraw()

    def turns(self):
        '''Dispalys which player turn it currently is'''
        if self.turn % 2 == 1:
            self.square.setStyleSheet("QWidget { background-color: #fff }")
            self.turn + 1

        else:
            self.square.setStyleSheet("QWidget { background-color: #000 }")
            self.turn + 1

        self.currTurn.update
