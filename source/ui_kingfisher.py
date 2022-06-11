# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kingfisher_uiwUtjBr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2887, 1209)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.kingfisher = QLabel(self.centralwidget)
        self.kingfisher.setObjectName(u"kingfisher")
        self.kingfisher.setGeometry(QRect(450, 350, 81, 81))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.kingfisher.setText(QCoreApplication.translate("MainWindow", u"kingfisher", None))
    # retranslateUi

