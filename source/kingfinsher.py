import win32gui
from ui_kingfisher import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
#Created by hadi muhammed
import PySide2
import sys
import random
import PyQt5.QtCore as core
from PyQt5.QtCore import pyqtSignal
from iconify.qt import QtGui,QtWidgets,QtCore
from time import sleep
window = []
win_list = []
follower = ""
ufo_size_y = 120
ufo_size_x = 120
xx = 0
yy = 0
bx = 0
bird_R = "./gif/bird_r.gif"
bird_L = "./gif/bird_l.gif"
#print(QWidget.mapFromGlobal(QtCore.QPoint(10,10)))



        

                    
            



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global bx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        
        #UFO
        self.ui.kingfisher.setScaledContents(True);
        self.ui.kingfisher.setToolTip("kukkooo")
        self.ui.kingfisher.setToolTipDuration(10000)        
        self.ui.kingfisher.setScaledContents(True)
        self.bird = QtGui.QMovie(bird_R)
        self.ui.kingfisher.setMovie(self.bird)
        self.bird.start()
        
        self.ufo_obj = self.ui.kingfisher
        bx = self.ufo_obj.x()
        self.ufo_anim_group = QSequentialAnimationGroup() 
        self.animation_starting = QPropertyAnimation(self.ufo_obj,b'geometry')
        self.animation_after = QPropertyAnimation(self.ufo_obj,b'geometry')

        self.animation_after.finished.connect(self.bird_animate_)

        self.show() 
                       
    def bird_left(self):
        self.bird = QtGui.QMovie(bird_L)
        self.ui.kingfisher.setMovie(self.bird)
        self.bird.start() 
    def bird_right(self):
        self.bird = QtGui.QMovie(bird_R)
        self.ui.kingfisher.setMovie(self.bird)
        self.bird.start()         
        
    def bird_animate(self,x,y):
        self.animation_starting.setDuration(3000)
        self.animation_after.setDuration(2000)
        self.animation_starting.setEasingCurve(QEasingCurve.OutCubic)
        self.animation_after.setEasingCurve(QEasingCurve.OutCubic)
        self.animation_starting.setEndValue(QRect(self.ufo_obj.x(),self.ufo_obj.y(),ufo_size_y,ufo_size_x))
        self.animation_after.setEndValue(QRect(x-70,y-70,ufo_size_y,ufo_size_x))
        
        
        self.ufo_anim_group.addAnimation(self.animation_starting)
        self.ufo_anim_group.addAnimation(self.animation_after)
        self.ufo_anim_group.start()         


    def bird_animate_(self):
        win32gui.EnumWindows(callback, None)
        #pass
def callback(hwnd, extra):
    
    global xx,yy,bx,follower
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    follower = win32gui.GetWindowText(win32gui.GetForegroundWindow())    
    if follower.lower() in str(win32gui.GetWindowText(hwnd)).lower():
            print(follower)
            point = QtCore.QPoint(x, y)
            widget = window.mapFromGlobal(point)        
            if widget.x() < window.ufo_obj.x():
                window.bird_left()
                bx = window.ufo_obj.x()
            else:
                window.bird_right()
                bx = window.ufo_obj.x()       
            window.bird_animate(widget.x(),widget.y())
if __name__ == "__main__":
        #)
        app = QApplication(sys.argv)
        window = MainWindow()
        win32gui.EnumWindows(callback, None)
        sys.exit(app.exec_())