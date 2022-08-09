# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_crtype.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_crtype(object):
    def setupUi(self, crtype):
        if not crtype.objectName():
            crtype.setObjectName(u"crtype")
        crtype.resize(1115, 532)
        crtype.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.btn_save = QPushButton(crtype)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(260, 360, 101, 24))
        self.btn_save.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_single = QRadioButton(crtype)
        self.rd_single.setObjectName(u"rd_single")
        self.rd_single.setGeometry(QRect(20, 390, 89, 20))
        self.rd_single.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_ask = QPushButton(crtype)
        self.btn_import_ask.setObjectName(u"btn_import_ask")
        self.btn_import_ask.setGeometry(QRect(140, 450, 101, 24))
        self.btn_import_ask.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_court = QPushButton(crtype)
        self.btn_import_court.setObjectName(u"btn_import_court")
        self.btn_import_court.setGeometry(QRect(140, 480, 101, 24))
        self.btn_import_court.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_kics = QPushButton(crtype)
        self.btn_import_kics.setObjectName(u"btn_import_kics")
        self.btn_import_kics.setGeometry(QRect(140, 390, 101, 24))
        self.btn_import_kics.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_112 = QPushButton(crtype)
        self.btn_import_112.setObjectName(u"btn_import_112")
        self.btn_import_112.setGeometry(QRect(140, 360, 101, 24))
        self.btn_import_112.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_random = QTextEdit(crtype)
        self.edit_random.setObjectName(u"edit_random")
        self.edit_random.setGeometry(QRect(20, 30, 441, 161))
        self.edit_random.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.label_8 = QLabel(crtype)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 340, 91, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_paragraph = QRadioButton(crtype)
        self.rd_paragraph.setObjectName(u"rd_paragraph")
        self.rd_paragraph.setGeometry(QRect(20, 360, 89, 20))
        self.rd_paragraph.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(crtype)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(crtype)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 340, 91, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_news = QPushButton(crtype)
        self.btn_import_news.setObjectName(u"btn_import_news")
        self.btn_import_news.setGeometry(QRect(140, 420, 101, 24))
        self.btn_import_news.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.plainTextEdit_4 = QPlainTextEdit(crtype)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(770, 230, 331, 101))
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(255, 182, 148);")
        self.label_3 = QLabel(crtype)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 200, 131, 16))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_crtype = QPushButton(crtype)
        self.btn_import_crtype.setObjectName(u"btn_import_crtype")
        self.btn_import_crtype.setGeometry(QRect(70, 200, 101, 24))
        self.btn_import_crtype.setStyleSheet(u"background-color: rgb(255, 251, 212);")
        self.edit_crtype = QTextEdit(crtype)
        self.edit_crtype.setObjectName(u"edit_crtype")
        self.edit_crtype.setGeometry(QRect(20, 230, 441, 101))
        self.edit_crtype.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.plainTextEdit = QPlainTextEdit(crtype)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(470, 230, 291, 101))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 182, 148);")
        self.btn_standard = QPushButton(crtype)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setGeometry(QRect(180, 200, 101, 24))
        self.btn_standard.setStyleSheet(u"background-color: rgb(255, 251, 212)")

        self.retranslateUi(crtype)

        QMetaObject.connectSlotsByName(crtype)
    # setupUi

    def retranslateUi(self, crtype):
        crtype.setWindowTitle(QCoreApplication.translate("crtype", u"crtype", None))
        self.btn_save.setText(QCoreApplication.translate("crtype", u"\uc800\uc7a5", None))
        self.rd_single.setText(QCoreApplication.translate("crtype", u"\ubb38\uc7a5\uc218\uc900", None))
        self.btn_import_ask.setText(QCoreApplication.translate("crtype", u"\uace0\uac1d\ub9cc\uc871, \uc124\ubb38", None))
        self.btn_import_court.setText(QCoreApplication.translate("crtype", u"\ud310\uacb0\ubb38", None))
        self.btn_import_kics.setText(QCoreApplication.translate("crtype", u"KICS\ubc94\uc8c4\uc0ac\uc2e4", None))
        self.btn_import_112.setText(QCoreApplication.translate("crtype", u"112 \uc811\uc218\uc0ac\uc2e4", None))
        self.label_8.setText(QCoreApplication.translate("crtype", u"\ub2e8\uc704\uc124\uc815", None))
        self.rd_paragraph.setText(QCoreApplication.translate("crtype", u"\ubb38\ub2e8\uc218\uc900", None))
        self.label.setText(QCoreApplication.translate("crtype", u"Random Text", None))
        self.label_4.setText(QCoreApplication.translate("crtype", u"\ud14d\uc2a4\ud2b8 \ubd88\ub7ec\uc624\uae30", None))
        self.btn_import_news.setText(QCoreApplication.translate("crtype", u"\ub124\uc774\ubc84 \ub274\uc2a4", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("crtype", u"<\uc124\uba85>\n"
"\uac15\ub825\ubc94\uc8c4 : \uac15\ub3c4, \ubc29\ud654, \uc0b4\uc778, \uac15\uac04, \uac15\uc81c\ucd94\ud589\n"
"\uc9c0\ub2a5\ubc94\uc8c4 : \uc0ac\uae30, \ud6a1\ub839, \ubc30\uc784, \uc9c1\uad8c\ub0a8\uc6a9, \uc9c1\ubb34\uc720\uae30, \ub1cc\ubb3c \ub4f1\n"
"\ud2b9\ubcc4\uacbd\uc81c\ubc94\uc8c4 : \ubd80\uc815\uc218\ud45c, \uacbd\ub9e4\ubc29\ud574, \ud2b9\uac00\ubc95(\uad00\uc138) \ub4f1\n"
"\ud3ed\ub825\ubc94\uc8c4 : \ud3ed\ud589, \uc544\ub3d9\ud559\ub300 \ub4f1", None))
        self.label_3.setText(QCoreApplication.translate("crtype", u"\uc8c4\uc885(1)", None))
        self.btn_import_crtype.setText(QCoreApplication.translate("crtype", u"\uc8c4\uba85\uac80\uc0c9\ud558\uae30", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("crtype", u"<\ub300\ubd84\ub958>\n"
"\ubc94\uc8c4\uc544\ub2d8 / \uac15\ub825\ubc94\uc8c4 / \uc808\ub3c4\ubc94\uc8c4 / \uad50\ud1b5\ubc94\uc8c4 / \uc9c0\ub2a5\ubc94\uc8c4 / \uae30\ud0c0\ubc94\uc8c4 / \ud3ed\ub825\ubc94\uc8c4 / \uc120\uac70\ubc94\uc8c4 / \ub178\ub3d9\ubc94\uc8c4 / \ud658\uacbd\ubc94\uc8c4 / \ubcd1\uc5ed\ubc94\uc8c4 / \ud2b9\ubcc4\uacbd\uc81c\ubc94\uc8c4 / \uc548\ubcf4\ubc94\uc8c4 / \ud48d\uc18d\ubc94\uc8c4 / \ubcf4\uac74\ubc94\uc8c4 / \ub9c8\uc57d\ubc94\uc8c4", None))
        self.btn_standard.setText(QCoreApplication.translate("crtype", u"\uae30\uc900\ub9cc\ub4e4\uae30", None))
    # retranslateUi

