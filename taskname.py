# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskname.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_ner = QPushButton(self.centralwidget)
        self.btn_ner.setObjectName(u"btn_ner")
        self.btn_ner.setGeometry(QRect(130, 130, 151, 81))
        self.btn_ner.setStyleSheet(u"background-color: rgb(255, 182, 148);\n"
"font: 13pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_keyword = QPushButton(self.centralwidget)
        self.btn_keyword.setObjectName(u"btn_keyword")
        self.btn_keyword.setGeometry(QRect(310, 130, 151, 81))
        self.btn_keyword.setStyleSheet(u"background-color: rgb(255, 182, 148);\n"
"font: 13pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_sentence = QPushButton(self.centralwidget)
        self.btn_sentence.setObjectName(u"btn_sentence")
        self.btn_sentence.setGeometry(QRect(490, 130, 151, 81))
        self.btn_sentence.setStyleSheet(u"background-color: rgb(255, 182, 148);\n"
"font: 13pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_crtype = QPushButton(self.centralwidget)
        self.btn_crtype.setObjectName(u"btn_crtype")
        self.btn_crtype.setGeometry(QRect(130, 240, 151, 81))
        self.btn_crtype.setStyleSheet(u"background-color: rgb(255, 182, 148);\n"
"font: 13pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 70, 151, 41))
        self.label.setStyleSheet(u"font: 22pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.btn_legal = QPushButton(self.centralwidget)
        self.btn_legal.setObjectName(u"btn_legal")
        self.btn_legal.setGeometry(QRect(310, 240, 151, 81))
        self.btn_legal.setStyleSheet(u"background-color: rgb(255, 182, 148);\n"
"font: 13pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_court = QPushButton(self.centralwidget)
        self.btn_court.setObjectName(u"btn_court")
        self.btn_court.setGeometry(QRect(490, 240, 151, 81))
        self.btn_court.setStyleSheet(u"background-color: rgb(255, 182, 148);\n"
"font: 13pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_idea = QPushButton(self.centralwidget)
        self.btn_idea.setObjectName(u"btn_idea")
        self.btn_idea.setGeometry(QRect(310, 350, 151, 81))
        self.btn_idea.setStyleSheet(u"background-color: rgb(221, 255, 245);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Police Natural Language Process", None))
        self.btn_ner.setText(QCoreApplication.translate("MainWindow", u"NER", None))
        self.btn_keyword.setText(QCoreApplication.translate("MainWindow", u"KEYWORD", None))
        self.btn_sentence.setText(QCoreApplication.translate("MainWindow", u"Sentence Attribute", None))
        self.btn_crtype.setText(QCoreApplication.translate("MainWindow", u"Crime Type", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Task Name", None))
        self.btn_legal.setText(QCoreApplication.translate("MainWindow", u"Legal Provision", None))
        self.btn_court.setText(QCoreApplication.translate("MainWindow", u"Related Court", None))
        self.btn_idea.setText(QCoreApplication.translate("MainWindow", u"Additional Task IDEA", None))
    # retranslateUi

