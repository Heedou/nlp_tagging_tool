# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_keyword.ui'
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

class Ui_keyword(object):
    def setupUi(self, keyword):
        if not keyword.objectName():
            keyword.setObjectName(u"keyword")
        keyword.resize(498, 628)
        keyword.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.btn_save = QPushButton(keyword)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(260, 440, 101, 24))
        self.btn_save.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_news = QPushButton(keyword)
        self.btn_import_news.setObjectName(u"btn_import_news")
        self.btn_import_news.setGeometry(QRect(140, 500, 101, 24))
        self.btn_import_news.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_ask = QPushButton(keyword)
        self.btn_import_ask.setObjectName(u"btn_import_ask")
        self.btn_import_ask.setGeometry(QRect(140, 530, 101, 24))
        self.btn_import_ask.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.plainTextEdit_3 = QPlainTextEdit(keyword)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(20, 230, 251, 61))
        self.plainTextEdit_3.setStyleSheet(u"background-color: rgb(255, 206, 166);")
        self.rd_paragraph = QRadioButton(keyword)
        self.rd_paragraph.setObjectName(u"rd_paragraph")
        self.rd_paragraph.setGeometry(QRect(20, 440, 89, 20))
        self.rd_paragraph.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_112 = QPushButton(keyword)
        self.btn_import_112.setObjectName(u"btn_import_112")
        self.btn_import_112.setGeometry(QRect(140, 440, 101, 24))
        self.btn_import_112.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(keyword)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 200, 131, 16))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(keyword)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 420, 91, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_single = QRadioButton(keyword)
        self.rd_single.setObjectName(u"rd_single")
        self.rd_single.setGeometry(QRect(20, 470, 89, 20))
        self.rd_single.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(keyword)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 420, 91, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(keyword)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_keyword = QTextEdit(keyword)
        self.edit_keyword.setObjectName(u"edit_keyword")
        self.edit_keyword.setGeometry(QRect(20, 300, 441, 101))
        self.edit_keyword.setStyleSheet(u"color: rgb(255, 255, 255);font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_import_court = QPushButton(keyword)
        self.btn_import_court.setObjectName(u"btn_import_court")
        self.btn_import_court.setGeometry(QRect(140, 560, 101, 24))
        self.btn_import_court.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_kics = QPushButton(keyword)
        self.btn_import_kics.setObjectName(u"btn_import_kics")
        self.btn_import_kics.setGeometry(QRect(140, 470, 101, 24))
        self.btn_import_kics.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_random = QTextEdit(keyword)
        self.edit_random.setObjectName(u"edit_random")
        self.edit_random.setGeometry(QRect(20, 30, 441, 161))
        self.edit_random.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_import_112voice = QPushButton(keyword)
        self.btn_import_112voice.setObjectName(u"btn_import_112voice")
        self.btn_import_112voice.setGeometry(QRect(140, 590, 101, 24))
        self.btn_import_112voice.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_standard = QPushButton(keyword)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setGeometry(QRect(120, 200, 101, 24))
        self.btn_standard.setStyleSheet(u"background-color: rgb(255, 251, 212)")

        self.retranslateUi(keyword)

        QMetaObject.connectSlotsByName(keyword)
    # setupUi

    def retranslateUi(self, keyword):
        keyword.setWindowTitle(QCoreApplication.translate("keyword", u"keyword", None))
        self.btn_save.setText(QCoreApplication.translate("keyword", u"\uc800\uc7a5", None))
        self.btn_import_news.setText(QCoreApplication.translate("keyword", u"\ub124\uc774\ubc84 \ub274\uc2a4", None))
        self.btn_import_ask.setText(QCoreApplication.translate("keyword", u"\uace0\uac1d\ub9cc\uc871, \uc124\ubb38", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("keyword", u"<\ud0a4\uc6cc\ub4dc>\n"
"\uc911\uc694\ud558\ub2e4\uace0 \uc0dd\uac01\ub418\ub294 '\ub2e8\uc5b4'\uc5d0\ub9cc <>\ub85c \uccb4\ud06c", None))
        self.rd_paragraph.setText(QCoreApplication.translate("keyword", u"\ubb38\ub2e8\uc218\uc900", None))
        self.btn_import_112.setText(QCoreApplication.translate("keyword", u"112 \uc811\uc218\uc0ac\uc2e4", None))
        self.label_6.setText(QCoreApplication.translate("keyword", u"Keyword Tagging", None))
        self.label_4.setText(QCoreApplication.translate("keyword", u"\ud14d\uc2a4\ud2b8 \ubd88\ub7ec\uc624\uae30", None))
        self.rd_single.setText(QCoreApplication.translate("keyword", u"\ubb38\uc7a5\uc218\uc900", None))
        self.label_8.setText(QCoreApplication.translate("keyword", u"\ub2e8\uc704\uc124\uc815", None))
        self.label.setText(QCoreApplication.translate("keyword", u"Random Text", None))
        self.btn_import_court.setText(QCoreApplication.translate("keyword", u"\ud310\uacb0\ubb38", None))
        self.btn_import_kics.setText(QCoreApplication.translate("keyword", u"KICS\ubc94\uc8c4\uc0ac\uc2e4", None))
        self.btn_import_112voice.setText(QCoreApplication.translate("keyword", u"112 \ubcf4\uc774\uc2a4\ud53c\uc2f1", None))
        self.btn_standard.setText(QCoreApplication.translate("keyword", u"\uae30\uc900\ub9cc\ub4e4\uae30", None))
    # retranslateUi

