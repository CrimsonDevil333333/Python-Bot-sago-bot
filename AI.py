p=print
f=False
t=True
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
import sys
import random
from random import randrange
from tkinter import *
import math
from PyQt5 import QtCore, QtGui, QtWidgets
import pafy, pyglet
import urllib.request
from urllib.parse import *
from bs4 import BeautifulSoup
from turtle import *
from datetime import datetime
import os
import random
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSound
from Dialog import *
from tictactoe_ui import Ui_tictactoe



class Game(QMainWindow, Ui_tictactoe):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.turn = None
        self.timer = QTimer()

      
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.sounds = dict(circle=QSound("circle.wav"),
                           cross=QSound("cross.wav"),
                           win=QSound("win.wav"),
                           lose=QSound("lose.wav"))

        xIconPath = os.path.join("Icons", "x.png")
        oIconPath = os.path.join("Icons", "o.png")

        self.xIcon = QIcon(xIconPath)
        self.oIcon = QIcon(oIconPath)

     
        self.xIcon.addPixmap(QPixmap(xIconPath), QIcon.Disabled)
        self.oIcon.addPixmap(QPixmap(oIconPath), QIcon.Disabled)

        self.allButtons = self.frame.findChildren(QToolButton)
        self.availabeButtons = self.allButtons[:]
        self.defaultPalette = QApplication.palette()


        self.buttonGroup1 = [
            self.button1, self.button2, self.button3]

      
        self.buttonGroup2 = [
            self.button4, self.button5, self.button6]

      
        self.buttonGroup3 = [
            self.button7, self.button8, self.button9]

     
        self.buttonGroup4 = [
            self.button1, self.button4, self.button7]

       
        self.buttonGroup5 = [
            self.button2, self.button5, self.button8]

      
        self.buttonGroup6 = [
            self.button3, self.button6, self.button9]


        self.buttonGroup7 = [
            self.button1, self.button5, self.button9]


        self.buttonGroup8 = [
            self.button3, self.button5, self.button7]


        for button in self.allButtons:
            button.clicked.connect(self.button_clicked)

        self.actionNew_Game.triggered.connect(self.new_game)
        self.actionDark_Theme.toggled.connect(self.dark_theme)
        self.action_Exit.triggered.connect(self.close)

        self.setFocus()
        self.new_game()

    def new_game(self):
        self.reset()
        self.turn = 1

    def reset(self):
        self.turn = None
        self.frame.setEnabled(True)
        self.availabeButtons = self.allButtons[:]

        for button in self.availabeButtons:
            button.setText("")
            button.setIcon(QIcon())
            button.setEnabled(True)

    def check(self):
        if self.check_list(self.buttonGroup1):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup2):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup3):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup4):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup5):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup6):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup7):
            return self.end_game(self.turn)

        elif self.check_list(self.buttonGroup8):
            return self.end_game(self.turn)

    def check_list(self, lst):
        for member in lst:
            if member.text() != str(self.turn):
                return False
        return True

    def end_game(self, state):
        """Ends the game"""

        if state == 1:
            self.sounds["win"].play()
            Dialog(self, state).show()

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 2:
            self.sounds["lose"].play()
            Dialog(self, state).show()

            for button in self.availabeButtons:
                button.setEnabled(False)
            self.availabeButtons.clear()
            return True

        elif state == 3:
            Dialog(self, state).show()

            for button in self.allButtons:
                button.setEnabled(False)
            return True
        return False

    def button_clicked(self):
        button = self.sender()

        self.sounds["cross"].play()

        button.setText("1")
        button.setIcon(self.xIcon)
        button.setEnabled(False)
        self.availabeButtons.remove(button)

        if self.check():
            return

        self.turn = 2
        self.frame.setEnabled(False)

        self.timer.singleShot(400, self.com_play)

    def com_play(self):
        try:
            random_button = random.choice(self.availabeButtons)
        except: 
            self.end_game(3)
            return

        self.sounds["circle"].play()
        random_button.setText("2")
        random_button.setIcon(self.oIcon)
        random_button.setEnabled(False)
        self.availabeButtons.remove(random_button)

        if self.check():
            return
        self.frame.setEnabled(True)
        self.turn = 1

    def dark_theme(self):
        """Changes the theme between dark and normal"""
        if self.actionDark_Theme.isChecked():
            QApplication.setStyle(QStyleFactory.create("Fusion"))
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(15, 15, 15))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Highlight, QColor(0, 24, 193).lighter())
            palette.setColor(QPalette.HighlightedText, Qt.black)
            palette.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
            palette.setColor(
                QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
            app.setPalette(palette)
            return

        app.setPalette(self.defaultPalette)


def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze)
    lt(120)
    fd(spitze/2.0)

def make_hand_shape(name, laenge, spitze):
    reset()
    jump(-laenge*0.15)
    begin_poly()
    hand(laenge, spitze)
    end_poly()
    hand_form = get_poly()
    register_shape(name, hand_form)

def clockface(radius):
    reset()
    pensize(7)
    for i in range(60):
        jump(radius)
        if i % 5 == 0:
            fd(25)
            jump(-radius-25)
        else:
            dot(3)
            jump(-radius)
        rt(6)

def setup():
    global second_hand, minute_hand, hour_hand, writer
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    clockface(160)
    second_hand = Turtle()
    second_hand.shape("second_hand")
    second_hand.color("gray20", "gray80")
    minute_hand = Turtle()
    minute_hand.shape("minute_hand")
    minute_hand.color("blue1", "red1")
    hour_hand = Turtle()
    hour_hand.shape("hour_hand")
    hour_hand.color("blue3", "red3")
    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    ht()
    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.bk(85)

def wochentag(t):
    wochentag = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentag[t.weekday()]

def datum(z):
    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    j = z.year
    m = monat[z.month - 1]
    t = z.day
    return "%s %d %d" % (m, t, j)

def tick():
    t = datetime.today()
    sekunde = t.second + t.microsecond*0.000001
    minute = t.minute + sekunde/60.0
    stunde = t.hour + minute/60.0
    try:
        tracer(False)  # Terminator can occur here
        writer.clear()
        writer.home()
        writer.forward(65)
        writer.write(wochentag(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.back(150)
        writer.write(datum(t),
                     align="center", font=("Courier", 14, "bold"))
        writer.forward(85)
        tracer(True)
        second_hand.setheading(6*sekunde)  # or here
        minute_hand.setheading(6*minute)
        hour_hand.setheading(30*stunde)
        tracer(True)
        ontimer(tick, 100)
    except Terminator:
        pass  # turtledemo user pressed STOP

def mains():
    tracer(False)
    setup()
    tracer(True)
    tick()
    return "EVENTLOOP"

def chearsong(l):
    ################################  VLC   ##############################
    p("wait sir")

def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)

def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"


class Youtube_mp3():
    def __init__(self):
        self.lst = []
        self.dict = {}
        self.dict_names = {}
        self.playlist = []

    def url_search(self, search_string, max_search):
        textToSearch = search_string
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        i = 1
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            if len(self.dict) < max_search:
                self.dict[i] = 'https://www.youtube.com' + vid['href']
                i += 1
            else:
                break


    def get_search_items(self, max_search):

        if self.dict != {}:
            i = 1
            for url in self.dict.values():
                try:
                    info = pafy.new(url)
                    self.dict_names[i] = info.title
                    print("{0}. {1}".format(i, info.title))
                    i += 1

                except ValueError:
                    pass

    def play_media(self, num):
        url = self.dict[int(num)]
        info = pafy.new(url)

        audio = info.getbestaudio(preftype="m4a")
        audio.download('song.m4a', quiet=True)
        song = pyglet.media.load('song.m4a')
        player = pyglet.media.Player()
        player.queue(song)
        print("Playing: {0}.".format(self.dict_names[int(num)]))
        player.play()
        stop = ''
        while True:
            stop = input('Type "s" to stop; "p" to pause; "" to play; : ')
            if stop == 's':
                player.pause()
                break
            elif stop == 'p':
                player.pause()
            elif stop == '':
                player.play()
            elif stop == 'r':
    
                print('Replaying: {0}'.format(self.dict_names[int(num)]))
                




    def download_media(self, num):
        url = self.dict[int(num)]
        info = pafy.new(url)
        audio = info.getbestaudio(preftype="m4a")
        song_name = self.dict_names[int(num)]
        print("Downloading: {0}.".format(self.dict_names[int(num)]))
        print(song_name)
        song_name = input("Filename (Enter if as it is): ")

        file_name = song_name + '.m4a'
        if song_name == '':
            audio.download(remux_audio=True)
        else:
            audio.download(filepath = filename, remux_audio=True)


    def bulk_download(self, url):
        info = pafy.new(url)
        audio = info.getbestaudio(preftype="m4a")
        song_name = self.dict_names[int(num)]
        print("Downloading: {0}.".format(self.dict_names[int(num)]))
        print(song_name)
        song_name = input("Filename (Enter if as it is): ")

        file_name = song_name + '.m4a'
        if song_name == '':
            audio.download(remux_audio=True)
        else:
            audio.download(filepath = filename, remux_audio=True)

    def add_playlist(self, search_query):
        url = self.url_search(search_query, max_search=1)
        self.playlist.append(url)





class Tetris(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):    
        '''initiates application UI'''

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()        
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        
        self.tboard.start()
        
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')        
        self.show()
        

    def center(self):
        '''centers the window on the screen'''
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, 
            (screen.height()-size.height())/2)
        

class Board(QFrame):
    
    msg2Statusbar = pyqtSignal(str)
    
    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)
        
        self.initBoard()
        
        
    def initBoard(self):     
        '''initiates board'''

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False
        
        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()
        
        
    def shapeAt(self, x, y):
        '''determines shape at the board position'''
        
        return self.board[(y * Board.BoardWidth) + x]

        
    def setShapeAt(self, x, y, shape):
        '''sets a shape at the board'''
        
        self.board[(y * Board.BoardWidth) + x] = shape
        

    def squareWidth(self):
        '''returns the width of one square'''
        
        return self.contentsRect().width() // Board.BoardWidth
        

    def squareHeight(self):
        '''returns the height of one square'''
        
        return self.contentsRect().height() // Board.BoardHeight
        

    def start(self):
        '''starts game'''
        
        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)

        
    def pause(self):
        '''pauses game'''
        
        if not self.isStarted:
            return

        self.isPaused = not self.isPaused
        
        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")
            
        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()

        
    def paintEvent(self, event):
        '''paints all shapes of the game'''
        
        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)
                
                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:
            
            for i in range(4):
                
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())

                    
    def keyPressEvent(self, event):
        '''processes key press events'''
        
        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()
        
        if key == Qt.Key_P:
            self.pause()
            return
            
        if self.isPaused:
            return
                
        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)
            
        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)
            
        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)
            
        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)
            
        elif key == Qt.Key_Space:
            self.dropDown()
            
        elif key == Qt.Key_D:
            self.oneLineDown()
            
        else:
            super(Board, self).keyPressEvent(event)
                

    def timerEvent(self, event):
        '''handles timer event'''
        
        if event.timerId() == self.timer.timerId():
            
            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()
                
        else:
            super(Board, self).timerEvent(event)

            
    def clearBoard(self):
        '''clears shapes from the board'''
        
        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)

        
    def dropDown(self):
        '''drops down a shape'''
        
        newY = self.curY
        
        while newY > 0:
            
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
                
            newY -= 1

        self.pieceDropped()
        

    def oneLineDown(self):
        '''goes one line down with a shape'''
        
        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()
            

    def pieceDropped(self):
        '''after dropping shape, remove full lines and create new shape'''
        
        for i in range(4):
            
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()
            

    def removeFullLines(self):
        '''removes all full lines from the board'''
        
        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):
            
            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()
        

        for m in rowsToRemove:
            
            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:
            
            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))
                
            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()
            

    def newPiece(self):
        '''creates a new shape'''
        
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()
        
        if not self.tryMove(self.curPiece, self.curX, self.curY):
            
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")



    def tryMove(self, newPiece, newX, newY):
        '''tries to move a shape'''
        
        for i in range(4):
            
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            
            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False
                
            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()
        
        return True
        

    def drawSquare(self, painter, x, y, shape):
        '''draws a square of a shape'''        
        
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2, 
            self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1, 
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7


class Shape(object):
    
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape

        self.setShape(Tetrominoe.NoShape)
        

    def shape(self):
        '''returns shape'''
        
        return self.pieceShape
        

    def setShape(self, shape):
        '''sets a shape'''
        
        table = Shape.coordsTable[shape]
        
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape
        

    def setRandomShape(self):
        '''chooses a random shape'''
        
        self.setShape(random.randint(1, 7))

        
    def x(self, index):
        '''returns x coordinate'''
        
        return self.coords[index][0]

        
    def y(self, index):
        '''returns y coordinate'''
        
        return self.coords[index][1]

        
    def setX(self, index, x):
        '''sets x coordinate'''
        
        self.coords[index][0] = x

        
    def setY(self, index, y):
        '''sets y coordinate'''
        
        self.coords[index][1] = y

        
    def minX(self):
        '''returns min x value'''
        
        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

        
    def maxX(self):
        '''returns max x value'''
        
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

        
    def minY(self):
        '''returns min y value'''
        
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

        
    def maxY(self):
        '''returns max y value'''
        
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m

        
    def rotateLeft(self):
        '''rotates shape to the left'''
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result

        
    def rotateRight(self):
        '''rotates shape to the right'''
        
        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape
        
        for i in range(4):
            
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Calender")
        Form.resize(401, 328)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 30, 401, 301))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("calender", "calender"))
        self.label.setText(_translate("Form", "Calender"))



class calc: 

	def getandreplace(self): 

		self.expression = self.e.get() 
		self.newtext=self.expression.replace('/','/') 
		self.newtext=self.newtext.replace('x','*')


	def equals(self): 
		self.getandreplace() 
		try: 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.e.delete(0,END) 
			self.e.insert(0,self.value) 

	def squareroot(self): 
		self.getandreplace() 
		try: 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.sqrtval=math.sqrt(self.value) 
			self.e.delete(0,END) 
			self.e.insert(0,self.sqrtval) 

	def square(self): 
		self.getandreplace() 
		try: 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.sqval=math.pow(self.value,2) 
			self.e.delete(0,END) 
			self.e.insert(0,self.sqval) 

	def clearall(self): 
			self.e.delete(0,END) 

	def clear1(self): 
			self.txt=self.e.get()[:-1] 
			self.e.delete(0,END) 
			self.e.insert(0,self.txt) 

	def action(self,argi): 
			self.e.insert(END,argi) 

	def __init__(self,master): 
			
			master.title('Calulator') 
			master.geometry() 
			self.e = Entry(master) 
			self.e.grid(row=0,column=0,columnspan=6,pady=3) 
			self.e.focus_set() 
			Button(master,text="=",width=11,height=3,fg="blue", 
				bg="orange",command=lambda:self.equals()).grid( 
									row=4, column=4,columnspan=2) 

			Button(master,text='AC',width=5,height=3, 
						fg="red", bg="light green", 
			command=lambda:self.clearall()).grid(row=1, column=4) 

			Button(master,text='C',width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.clear1()).grid(row=1, column=5) 

			Button(master,text="+",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action('+')).grid(row=4, column=3) 

			Button(master,text="x",width=5,height=3, 
					fg="blue",bg="orange", 
					command=lambda:self.action('x')).grid(row=2, column=3) 

			Button(master,text="-",width=5,height=3, 
					fg="red",bg="light green", 
					command=lambda:self.action('-')).grid(row=3, column=3) 

			Button(master,text="÷",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action('/')).grid(row=1, column=3) 

			Button(master,text="%",width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.action('%')).grid(row=4, column=2) 

			Button(master,text="7",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action('7')).grid(row=1, column=0) 

			Button(master,text="8",width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.action(8)).grid(row=1, column=1) 

			Button(master,text="9",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action(9)).grid(row=1, column=2) 

			Button(master,text="4",width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.action(4)).grid(row=2, column=0) 

			Button(master,text="5",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action(5)).grid(row=2, column=1) 

			Button(master,text="6",width=5,height=3, 
				fg="white",bg="blue", 
				command=lambda:self.action(6)).grid(row=2, column=2) 

			Button(master,text="1",width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.action(1)).grid(row=3, column=0) 

			Button(master,text="2",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action(2)).grid(row=3, column=1) 

			Button(master,text="3",width=5,height=3, 
				fg="white",bg="blue", 
				command=lambda:self.action(3)).grid(row=3, column=2) 

			Button(master,text="0",width=5,height=3, 
				fg="white",bg="blue", 
				command=lambda:self.action(0)).grid(row=4, column=0) 

			Button(master,text=".",width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.action('.')).grid(row=4, column=1) 

			Button(master,text="(",width=5,height=3, 
				fg="white",bg="blue", 
				command=lambda:self.action('(')).grid(row=2, column=4) 

			Button(master,text=")",width=5,height=3, 
				fg="blue",bg="orange", 
				command=lambda:self.action(')')).grid(row=2, column=5) 

			Button(master,text="?",width=5,height=3, 
				fg="red",bg="light green", 
				command=lambda:self.squareroot()).grid(row=3, column=4) 

			Button(master,text="x²",width=5,height=3, 
				fg="white",bg="blue", 
				command=lambda:self.square()).grid(row=3, column=5) 




def greetings(n):
    words_greetings=("hi","hello","hi i am your personal assistant how are you","hello sir")
    greetings=random.choice(words_greetings)
    p(greetings)

def pics(n):
    p("Enjoy!")
    
    root=Tk()
    root.title('Nature')
    label=Label(root, text="Hope You gonna like it")
    label.pack()
    
    imgs=("n1.gif","n2.gif","n3.gif","n4.gif","n5.gif","n6.gif")
    a=random.choice(imgs)
    photo=PhotoImage(file=a)
    labelphoto=Label(root,image=photo)
    labelphoto.pack()
    
    root.mainloop()
    
    p("*************")

def notepadop(n):
    p("*************************************************")
    f=open("notepad.txt",'r')
    p(f.read())
    p("*************************************************")

def notepad(n):
    f=open("notepad.txt",'w')
    a=input()
    f.write(a)
    p("to see what u wright just say 'show me what i typed' or 'what i told u to remeber' or 'show me my notes'")


def joke(n):
    words_joke=("wife-had your lunch \nhusband-had ur lunch\nwife- u r copying me \nhusband-you r copying me \nwife-lets go shoping \nhusband-i had my lunch","when i see lover names carved in tree\ni dont thhink it is sweet\ni just think how many people bring knifes on a DATE"
                ,"No more jokes sir","you have enough for today","you seriously think i can joke","maybe u think i can joke is a joke")
    joke=random.choice(words_joke)
    p(joke)

def friends(n):
    words_friend=("yes the one whome i am talking to","maybe sir","this is something i won't able to answer")
    friends=random.choice(words_friend)
    p(friends)

def hobby(n):
    words_hobby=("I wont have one","i am your assistant i can't have one","sorry to say bt none")
    hobby=random.choice(words_hobby)
    p(hobby)

def chat(n):
    words_chat=("ya r make me feeling ashamed","ya sir for you anytime","yup go ahead")
    chat=random.choice(words_chat)
    p(chat)

def animes(n):
    words_animes=("what do you mean that i mean of-course","ya sir u bet i do","are you doubting on my watching potentals")
    chats=random.choice(words_animes)
    p(chats)

def fun(n):
    words_fun=("make 32 and take it (pronounce 32 in hindi)")
    p(words_fun)

def animelike(n):
    words_likeanime=("i like some old clasic animes","i like naruto and their kids sho borutos","dragon balll z is not that bad","i wont gonna miss a chance to watch pokemon","you can suggest me some if u want to")
    aniee=random.choice(words_likeanime)
    p(aniee)

def dice(n):
    
    p("welcome this is a dice game")
    p("enter how many times you want to roll dice")
    q=eval(input())
    for i in range(0,q):
        value=randrange(1,6)
        p("+-------+")
        if value==1:
            p("|       |")
            p("|   *   |")
            p("|       |")
        if value==2:
            p("| *     |")
            p("|       |")
            p("|     * |")
        if value==3:
            p("| *     |")
            p("|   *   |")
            p("|     * |")
        if value==4:
            p("| *   * |")
            p("|       |")
            p("| *   * |")
        if value==5:
            p("| *   * |")
            p("|   *   |")
            p("| *   * |")
        if value==6:
            p("| *   * |")
            p("| *   * |")
            p("| *   * |")
        p("+-------+")


def randomno(n):
    p("give me a range of no\n")
    p("lower no = ")
    a=eval(input())
    p("higher no = ")
    b=eval(input())
    value=randrange(a,b)
    p("let me guess\n")
    p("i guess",value,"is your lucky no fr today")

def saveno(n):
    print("tell me the no u want to save")
    p("User : ",end="" )
    no=input()
    p("bot  : ",end="" )
    p("are you sure this is the no--", no ,"--you want to save?")
    p("bot  : ",end="" )
    p("if true say yes else no")
    p("User : ",end="" )
    response=input()
    if response=="yes" or response=="ya":
        m=no
        p("bot  : ",end="" )
        p(m,"-- has been saved")
        p("bot  : ",end="" )
        p("to view that no again just say 'show me that no' or 'which no i told you to remember'")
        return m
    if response=="no" or response=="nah":
        p("bot  : ",end="" )
        p("ok enter another no than")
        p("bot  : ",end="" )
        p("this is last try so try not to mess this time pls,")
        p("User : ",end="" )
        no=input()
        m=no
        p("bot  : ",end="" )
        p(m,"== has been saved")
        p("bot  : ",end="" )
        p("to view that no again just say 'show me that no' or 'which no i told you to remember'")
        return m
    return n
    
#under
#work
#please wait gonna comp soon
def pokemon(n):
    if n=="do you like pokemon":
        p("ya sir")
    if n=="see there is a pokemon":
        p("i am gonna try to catch it for you than")
    if n=="pokemon" or n=="pokemon game":
        p("if you want to play pokemon game say 'i want to play'")
        p("User : ",end="" )
        n=input()
        if n=="i want to play"or n=="bring it on" or n=="i want to play it":
            p("poke bot  : ",end="" )
            print("type 'help' or 'any tips' if you dont know how to play this game")
            m=True
            while m==True:
                p("User : ",end="" )
                n=input()
                if n=="help" or n=="how to quit" or n=="how to play this shit" or n=="any tips" or n=="i dont know how to play this game" or n=="how to play this game":
                    p("poke bot  : ",end="" )
                    p("this game is verry easy to play \nhere are some tips for you\n       1.just say 'i want to play','ok go ahead','thats gonna be fun' to start the game\n       2.after that sellect some pokeballs")
                    p("       3.a random pokemon gonna apear than\n       4.just say some magical words like 'catch app' or 'aim app' here app is that pokemon name")
                    p("\n       *keep that in mind that pokemon that gonna apear gonna have wrong spellings*")
                    p("\n       to quit say 'fuck off' or 'quit' or 'i am getting bored' or 'leave'")
                    p("User : ",end="" )
                    n=(input())
                    if n=="cool"or n=="awesome":
                        p("poke bot  : ",end="" )
                        p("you bet i am")
                if n=="ok i want to play it" or n=="i want to play" or n=="ok go ahead" or n=="thats gonna be fun":
                    p("poke bot  : ",end="" )
                    p("how many pokeball you want")
                    p("poke bot  : ",end="" )
                    p("select at least 10 pokeballs")
                    p("poke bot  : ",end="" )
                    p("enter 0 to quit")
                    ball=eval(input())
                    if(ball>10):
                        p("poke bot  : ",end="" )
                        p("now you have ",ball,"pokeballs")
                    else:
                        p("poke bot  : ",end="" )
                        p("select at least 10 next time")
                        p("       bye bye for now")
                        m==False
                if n=="how many balls i have now"or n=="no of balls" or n=="no of balls":
                        p(ball)
                if n=="quit" or n=="fuck off" or n=="i am getting bored" or n=="leave" or n==0:
                    m=False
            
        

p("Welcome sir i am your personal assistant")

while f==False:
    p("User : ",end="" )
    
    n=input()
    if n=="leave" or n=="close" or n=="thank u" or n=="by" or n=="fuck off":
        f=True
    if n=="hi" or n=="hello":
        p("bot  : ",end="" )
        greetings(n)
    if n=="what can u do" or n=="what can you do" or n=="what can i do in u" or n=="what shall i do in u":
        p("i can do many things like.")
        p("play games,open calc,casual chats,tell u a joke,pokemon game,open pics pics")
        p("open calculator,tetris game,tell feelings,share ur feelings,any hobbies,whats time")
        p("open notepad,tic tac toe,roll a dice,toss a coin,ying yang,calender")
    if n=="ying yang" or n=="open ying yang" or n=="ying and yang" or n=="dark and white":
        if __name__ == '__main__':
            main()
            mainloop()
    if n=="whats time" or n=="what is time" or n=="what time is it" or n=="tell me time":
        if __name__ == "__main__":
            mode("logo")
            msg = mains()
            print(msg)
            mainloop()
    if n=="toss a coin" or n=="head or tail":
        p("as ur wish sir")
        p("how many times u want to toss a coin")
        print("H=head,T=tail")
        q=eval(input())
        for i in range(0,q):
            value=randrange(1,2)
            if value==1:
                print("|       |")
                print("|   H   |")
                print("|       |")
            if value==2:
                print("|       |")
                print("|   T   |")
                print("|       |")
    if n=="tic tac toe" or n=="open tic tac toe" or n== "i want to play tic tac toe" or n=="ttt" or n=="play tic tac toe":
        app = QApplication(sys.argv)
        game = Game()
        game.show()
        app.exec_()
        
        




        
    if n=="tell me a joke" or n=="can u tell me a joke" or n=="entertain me" or n=="make me smile":
        p("bot  : ",end="" )
        joke(n)
    if n=="do you have any friends" or n=="are you single":
        p("bot  : ",end="" )
        friends(n)
    if n=="how are you" or n=="how u felling" or n=="how ya feeling" or n=="how r u feeling" or n=="how r u"or n=="how r you" or n=="how are u":
        p("bot  :I Am feeling \'FINE\' sir. But thanks for asking...\nbot  :IN bw how r u sir.")
    if n=="i am fine":
        p("bot  : ",end="" )
        p("I am Happy that u are fine else i will be worried")
    if n=="why u feel worried" or n=="worried?" or n=="worried" or n=="why worried":
        p("bot  : ",end="" )
        p("bcoz u r my master")
    if n=="glad u asked" or n=="glad u ask" or n=="glad you asked" or n=="glad u asked":
        p("bot  : ",end="" )
        p("Thanks \'SIR\'")
    if n=="i am nt feeling well" or n=="nt feeling well"or n=="nt well"or n=="not well"or n=="not feeling well":
        p("bot  : ",end="" )
        p("Can i sig a song for u if u r not feeling happy ?")
        o=True
        while o==True:
            p("User : ",end="" )
            l=input()
            if l=="yes":
                chearsong(l)
                o=False
            if l=="no" or n=="nah":
                o=False
    if n=="what is your hobby" or n=="whats your hobby" or n=="what is your leisure activity" or n=="what is ur hobby":
        p("bot  : ",end="" )
        hobby(n)
    if n=="do you have any hobby":
        p("bot  : ",end="" )
        p("nope")
    if n=="wanna have a little chat" or n=="do you have spare time for me" or n=="do you got any time on your hand" or n=="wanna have a talk" or n=="wanna chit chat" or n=="wanna goof around":
        p("bot  : ",end="" )
        chat(n)
    if n=="do you like animes" or n=="do u see animes" or n=="have you ever read mangas" or n=="do you love animes" or n=="have you ever seen hentai":
        p("bot  : ",end="" )
        animes(n)
    if n=="have you ever kicked a bucket" or n=="have you ever seen an ass":
        p("bot  : ",end="" )
        fun(n)
    if n=="have you ever had nose bleed":
        p("bot  : ",end="" )
        print("ya bt you dont wanna know when")
    if n=="no tell me" or n=="what do you mean by that" or n=="who the hell are you":
        p("bot  : ",end="" )
        p("leave it sir")
    if n=="have you ever feel home sickness" or n=="have you ever felt home sickness" or n=="have you ever felt nostalgia" or n=="do you  ever feel home sickness" or n=="do you ever feel nostlgia":
        p("bot  : ",end="" )
        p("ya when you are not with me and i talk to myself alone in off mode")
    if n=="what is your gender" or n=="are you male" or n=="are you female" or n=="you are female or male" or n=="you are male or female":
        p("bot  : ",end="" )
        p("i like to stay neutral")
    if n=="how are you feeling" or n=="how u like to stay" or n=="how you like to stay":
        p("bot  : ",end="" )
        p("i like to stay healthy")
    if n=="which animes do you like" or n=="which anime do u like":
        p("bot  : ",end="" )
        animelike(n)
    if n=="i am fine what about you":
        p("bot  : ",end="" )
        p("i am fine to")
    if n=="fine" or n=="i am fine" or n=="cool":
        p("bot  : ",end="" )
        p("glad to know  that")
    if n=="i am not feeling good" or n=="i am not feeling well" or n=="not well" or n=="i am nt fine":
        p("bot  : ",end="" )
        p("why what happened")
    if n=="nothing much" or n=="why i tell you":
        p("bot  : ",end="" )
        p("hmmmmm.....")
    if n=="do you like pokemon" or n=="pokemon game" or n=="pokemon" or n=="see there is a pokemon" or n=="have you ever seen pokemon":
        p("bot  : ",end="" )
        pokemon(n)
    if n=="roll a dice" or n=="dice game" or n=="whats on dice" or n=="what is on dice":
        p("bot  : ",end="" )
        dice(n)
    if n=="can you roll a dice":
        p("bot  : ",end="" )
        p("ya just say 'roll a dice' or 'dice game' or what is on dice")
    if n=="genrate a random no" or n=="guess a no for me" or n=="guess a no":
        p("bot  : ",end="" )
        randomno(n)
    if n=="can you guess a no for me" or n=="can you guess a random number for me" or n=="can u guess a random no fr me" or n=="can you guess a random no for me" or n=="can you guess a random no fr me":
        p("bot  : ",end="" )
        p("sure sir just say 'guess a no' or 'genrate a random no'")
    if n=="open calc" or n=="calculator" or n=="calc":
            p("bot  : ",end="" )
            p("why not sir\n")
            root = Tk() 
            obj=calc(root)
            root.mainloop()
            p("bot  : ",end="" )
            p("hope u have a good experiance")
    if n=="can you save a no for me":
        p("bot  : ",end="" )
        p("ya sure just say 'save this no' or 'save a no' and than type no you want to save")
        p("bot  : ",end="" )
        p("\n*saved no gonna be delete as soon as you turn me off")
    if n=="save this no"or n=="copy that no" or n=="save that no" or n=="remember that no" or n=="remember this no":
        p("bot  : ",end="" )
        saveno(n)
# if n=="show me that no" or n=="which no i told you to remember":

    if n=="can you open notepad" or n=="can i store something in you":
        p("bot  : ",end="" )
        p("ya sure just say 'open notepad' or 'type this' or 'save this' it is as easy as it sound")
    if n=="open notepad" or n=="save this" or n=="type this":
        p("bot  : ",end="" )
        notepad(n)
    if n=='show me what i typed' or n=='what i told u to remember' or n=='show me my notes':
        p("bot  : ",end="" )
        notepadop(n)
    if n=='show me some beautyfull pics' or n=="show me some pics" or n=="open pics" or n=="i want to see pics" or n=="nature" or n=="natural":
        p("bot  : ",end="" )
        p("dont blame me fr anything")
        pics(n)
    if n=="awsome" or n=="awesome":
        p("bot  : ",end="" )
        p("HaHa... thanks fr ur kind words sir")

    if n=="i want to play tetris" or n=="tetris" or n=="tetres" or n=="i want to play tetres" or n=="open tetris" or n=="open tetres":
        if __name__ == '__main__':
            app = QApplication([])
            tetris = Tetris()    
            sys.exit(app.exec_())
    if n=="open calender" or n=="whats today date" or n=="what is today date" or n=="calender":
        p("Hope u like it")
        if __name__ == "__main__":
            import sys
            app = QtWidgets.QApplication(sys.argv)
            Form = QtWidgets.QWidget()
            ui = Ui_Form()
            ui.setupUi(Form)
            Form.show()
            sys.exit(app.exec_())
        p("*********************")
    if n=="yor r the worst bot i ever seen" or n=="u sucks" or n=="u r worst":
        root=Tk()
        root.title('SAD')
        label=Label(root, text="This is what i am feeling at this moment...")
        label.pack()
        imgs=("s1.gif","s2.gif","s3.gif","s4.gif","s5.png")
        a=random.choice(imgs)
        photo=PhotoImage(file=a)
        labelphoto=Label(root,image=photo)
        labelphoto.pack() 
        root.mainloop()
    if n=="Play music" or n=="youtube" or n=="play this song" or n=="songs" or n=="utube" or n=="youtube music":
        if __name__ == '__main__':
            print('Welcome to the Youtube-Mp3 player.')
            x = Youtube_mp3()
            search = ''
            while search != 'q':
                search = input("Youtube Search: ")
                old_search = search
                max_search = 5
                x.dict = {}
                x.dict_names = {}

                if search == 'q':
                    print("Ending Youtube-Mp3 player.")
                    break

                download = input('1. Play Live Music\n2. Download Mp3 from Youtube.\n')
                if search != 'q' and (download == '1' or download == ''):
                    print('\nFetching for: {0} on youtube.'.format(search.title()))
                    x.url_search(search, max_search)
                    x.get_search_items(max_search)
                    song_number = input('Input song number: ')
                    x.play_media(song_number)
                elif download == '2':
                    print('\nDownloading {0} (conveniently) from youtube servers.'.format(search.title()))
                    x.url_search(search, max_search)
                    x.get_search_items(max_search)
                    song_number = input('Input song number: ')
                    x.download_media(song_number)




    
    p("\n")
        
    

