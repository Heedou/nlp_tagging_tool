# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_provision.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QWidget)

class Ui_provision(object):
    def setupUi(self, provision):
        if not provision.objectName():
            provision.setObjectName(u"provision")
        provision.resize(487, 529)
        provision.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.btn_import_news = QPushButton(provision)
        self.btn_import_news.setObjectName(u"btn_import_news")
        self.btn_import_news.setGeometry(QRect(140, 420, 101, 24))
        self.btn_import_news.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_court = QPushButton(provision)
        self.btn_import_court.setObjectName(u"btn_import_court")
        self.btn_import_court.setGeometry(QRect(140, 480, 101, 24))
        self.btn_import_court.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_ask = QPushButton(provision)
        self.btn_import_ask.setObjectName(u"btn_import_ask")
        self.btn_import_ask.setGeometry(QRect(140, 450, 101, 24))
        self.btn_import_ask.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(provision)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(provision)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 340, 91, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_random = QTextEdit(provision)
        self.edit_random.setObjectName(u"edit_random")
        self.edit_random.setGeometry(QRect(20, 30, 441, 161))
        self.edit_random.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_save = QPushButton(provision)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(260, 360, 101, 24))
        self.btn_save.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_single = QRadioButton(provision)
        self.rd_single.setObjectName(u"rd_single")
        self.rd_single.setGeometry(QRect(20, 390, 89, 20))
        self.rd_single.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_112 = QPushButton(provision)
        self.btn_import_112.setObjectName(u"btn_import_112")
        self.btn_import_112.setGeometry(QRect(140, 360, 101, 24))
        self.btn_import_112.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_kics = QPushButton(provision)
        self.btn_import_kics.setObjectName(u"btn_import_kics")
        self.btn_import_kics.setGeometry(QRect(140, 390, 101, 24))
        self.btn_import_kics.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(provision)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 340, 91, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_paragraph = QRadioButton(provision)
        self.rd_paragraph.setObjectName(u"rd_paragraph")
        self.rd_paragraph.setGeometry(QRect(20, 360, 89, 20))
        self.rd_paragraph.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_crname = QPushButton(provision)
        self.btn_import_crname.setObjectName(u"btn_import_crname")
        self.btn_import_crname.setGeometry(QRect(100, 200, 101, 24))
        self.btn_import_crname.setStyleSheet(u"background-color: rgb(255, 251, 212);")
        self.label_5 = QLabel(provision)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 200, 71, 16))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_law = QTextEdit(provision)
        self.edit_law.setObjectName(u"edit_law")
        self.edit_law.setGeometry(QRect(20, 230, 441, 101))
        self.edit_law.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_standard = QPushButton(provision)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setGeometry(QRect(210, 200, 101, 24))
        self.btn_standard.setStyleSheet(u"background-color: rgb(255, 251, 212)")

        self.retranslateUi(provision)

        QMetaObject.connectSlotsByName(provision)
    # setupUi

    def retranslateUi(self, provision):
        provision.setWindowTitle(QCoreApplication.translate("provision", u"provision", None))
        self.btn_import_news.setText(QCoreApplication.translate("provision", u"\ub124\uc774\ubc84 \ub274\uc2a4", None))
        self.btn_import_court.setText(QCoreApplication.translate("provision", u"\ud310\uacb0\ubb38", None))
        self.btn_import_ask.setText(QCoreApplication.translate("provision", u"\uace0\uac1d\ub9cc\uc871, \uc124\ubb38", None))
        self.label.setText(QCoreApplication.translate("provision", u"Random Text", None))
        self.label_8.setText(QCoreApplication.translate("provision", u"\ub2e8\uc704\uc124\uc815", None))
        self.btn_save.setText(QCoreApplication.translate("provision", u"\uc800\uc7a5", None))
        self.rd_single.setText(QCoreApplication.translate("provision", u"\ubb38\uc7a5\uc218\uc900", None))
        self.btn_import_112.setText(QCoreApplication.translate("provision", u"112 \uc811\uc218\uc0ac\uc2e4", None))
        self.btn_import_kics.setText(QCoreApplication.translate("provision", u"KICS\ubc94\uc8c4\uc0ac\uc2e4", None))
        self.label_4.setText(QCoreApplication.translate("provision", u"\ud14d\uc2a4\ud2b8 \ubd88\ub7ec\uc624\uae30", None))
        self.rd_paragraph.setText(QCoreApplication.translate("provision", u"\ubb38\ub2e8\uc218\uc900", None))
        self.btn_import_crname.setText(QCoreApplication.translate("provision", u"\uc870\ubb38\uac80\uc0c9\ud558\uae30", None))
        self.label_5.setText(QCoreApplication.translate("provision", u"\uad00\ub828\ubc95\uc870\ud56d", None))
        self.btn_standard.setText(QCoreApplication.translate("provision", u"\uae30\uc900\ub9cc\ub4e4\uae30", None))
    # retranslateUi

