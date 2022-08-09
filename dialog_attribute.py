# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_attribute.ui'
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

class Ui_attribute(object):
    def setupUi(self, attribute):
        if not attribute.objectName():
            attribute.setObjectName(u"attribute")
        attribute.resize(484, 616)
        attribute.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.btn_save = QPushButton(attribute)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(260, 460, 101, 24))
        self.btn_save.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_import_news = QPushButton(attribute)
        self.btn_import_news.setObjectName(u"btn_import_news")
        self.btn_import_news.setGeometry(QRect(140, 520, 101, 24))
        self.btn_import_news.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_ask = QPushButton(attribute)
        self.btn_import_ask.setObjectName(u"btn_import_ask")
        self.btn_import_ask.setGeometry(QRect(140, 550, 101, 24))
        self.btn_import_ask.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_paragraph = QRadioButton(attribute)
        self.rd_paragraph.setObjectName(u"rd_paragraph")
        self.rd_paragraph.setGeometry(QRect(20, 460, 89, 20))
        self.rd_paragraph.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_112 = QPushButton(attribute)
        self.btn_import_112.setObjectName(u"btn_import_112")
        self.btn_import_112.setGeometry(QRect(140, 460, 101, 24))
        self.btn_import_112.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(attribute)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 440, 91, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(attribute)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 210, 161, 16))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.plainTextEdit_5 = QPlainTextEdit(attribute)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(20, 240, 271, 81))
        self.plainTextEdit_5.setStyleSheet(u"background-color: rgb(255, 182, 148);")
        self.label_8 = QLabel(attribute)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 440, 91, 16))
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.rd_single = QRadioButton(attribute)
        self.rd_single.setObjectName(u"rd_single")
        self.rd_single.setGeometry(QRect(20, 490, 89, 20))
        self.rd_single.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(attribute)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_court = QPushButton(attribute)
        self.btn_import_court.setObjectName(u"btn_import_court")
        self.btn_import_court.setGeometry(QRect(140, 580, 101, 24))
        self.btn_import_court.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_kics = QPushButton(attribute)
        self.btn_import_kics.setObjectName(u"btn_import_kics")
        self.btn_import_kics.setGeometry(QRect(140, 490, 101, 24))
        self.btn_import_kics.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_random = QTextEdit(attribute)
        self.edit_random.setObjectName(u"edit_random")
        self.edit_random.setGeometry(QRect(20, 30, 441, 161))
        self.edit_random.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.edit_attribute = QTextEdit(attribute)
        self.edit_attribute.setObjectName(u"edit_attribute")
        self.edit_attribute.setGeometry(QRect(20, 330, 241, 101))
        self.edit_attribute.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.btn_standard = QPushButton(attribute)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setGeometry(QRect(180, 210, 101, 24))
        self.btn_standard.setStyleSheet(u"background-color: rgb(255, 251, 212)")

        self.retranslateUi(attribute)

        QMetaObject.connectSlotsByName(attribute)
    # setupUi

    def retranslateUi(self, attribute):
        attribute.setWindowTitle(QCoreApplication.translate("attribute", u"sentence attribute", None))
        self.btn_save.setText(QCoreApplication.translate("attribute", u"\uc800\uc7a5", None))
        self.btn_import_news.setText(QCoreApplication.translate("attribute", u"\ub124\uc774\ubc84 \ub274\uc2a4", None))
        self.btn_import_ask.setText(QCoreApplication.translate("attribute", u"\uace0\uac1d\ub9cc\uc871, \uc124\ubb38", None))
        self.rd_paragraph.setText(QCoreApplication.translate("attribute", u"\ubb38\ub2e8\uc218\uc900", None))
        self.btn_import_112.setText(QCoreApplication.translate("attribute", u"112 \uc811\uc218\uc0ac\uc2e4", None))
        self.label_4.setText(QCoreApplication.translate("attribute", u"\ud14d\uc2a4\ud2b8 \ubd88\ub7ec\uc624\uae30", None))
        self.label_7.setText(QCoreApplication.translate("attribute", u"\ubb38\uc7a5\uc18d\uc131(\ub2e8\ubb38\uc7a5\uc77c \uacbd\uc6b0\ub9cc)", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("attribute", u"<\uc18d\uc131>(\uc608)\n"
"\ub274\uc2a4 : \uc0ac\uac74\uae30\uc220 / \uc815\uce58\uc774\uc288 / \uac80\uacbd\uc758 \uc218\uc0ac\uc870\uce58\n"
"\ud310\ub840 : \uc0ac\uac74\uae30\uc220 / \ud310\uc0ac\ud310\ub2e8", None))
        self.label_8.setText(QCoreApplication.translate("attribute", u"\ub2e8\uc704\uc124\uc815", None))
        self.rd_single.setText(QCoreApplication.translate("attribute", u"\ubb38\uc7a5\uc218\uc900", None))
        self.label.setText(QCoreApplication.translate("attribute", u"Random Text", None))
        self.btn_import_court.setText(QCoreApplication.translate("attribute", u"\ud310\uacb0\ubb38", None))
        self.btn_import_kics.setText(QCoreApplication.translate("attribute", u"KICS\ubc94\uc8c4\uc0ac\uc2e4", None))
        self.btn_standard.setText(QCoreApplication.translate("attribute", u"\uae30\uc900\ub9cc\ub4e4\uae30", None))
    # retranslateUi

