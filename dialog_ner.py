# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_ner.ui'
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
    QSizePolicy, QTextBrowser, QTextEdit, QWidget)

class Ui_ner(object):
    def setupUi(self, ner):
        if not ner.objectName():
            ner.setObjectName(u"ner")
        ner.resize(1149, 797)
        ner.setStyleSheet(u"background-color: rgb(90, 90, 90);")
        self.label_4 = QLabel(ner)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 560, 91, 16))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser_5 = QTextBrowser(ner)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(960, 240, 171, 161))
        self.textBrowser_5.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.btn_save = QPushButton(ner)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(240, 580, 101, 24))
        self.btn_save.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser_8 = QTextBrowser(ner)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(490, 230, 271, 171))
        self.textBrowser_8.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.edit_random = QTextEdit(ner)
        self.edit_random.setObjectName(u"edit_random")
        self.edit_random.setGeometry(QRect(20, 30, 441, 221))
        self.edit_random.setStyleSheet(u"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"color: rgb(255, 255, 255);")
        self.textBrowser_6 = QTextBrowser(ner)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(770, 230, 181, 171))
        self.textBrowser_6.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.btn_import_112 = QPushButton(ner)
        self.btn_import_112.setObjectName(u"btn_import_112")
        self.btn_import_112.setGeometry(QRect(20, 580, 101, 24))
        self.btn_import_112.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.edit_tagging = QTextEdit(ner)
        self.edit_tagging.setObjectName(u"edit_tagging")
        self.edit_tagging.setGeometry(QRect(20, 310, 441, 241))
        self.edit_tagging.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 20pt \"\ub9d1\uc740 \uace0\ub515\";")
        self.textBrowser_2 = QTextBrowser(ner)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(690, 30, 261, 191))
        self.textBrowser_2.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.textBrowser_4 = QTextBrowser(ner)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(490, 410, 171, 111))
        self.textBrowser_4.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.textBrowser_7 = QTextBrowser(ner)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(490, 30, 191, 191))
        self.textBrowser_7.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.btn_handtagging = QPushButton(ner)
        self.btn_handtagging.setObjectName(u"btn_handtagging")
        self.btn_handtagging.setGeometry(QRect(130, 610, 101, 24))
        self.btn_handtagging.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_news = QPushButton(ner)
        self.btn_import_news.setObjectName(u"btn_import_news")
        self.btn_import_news.setGeometry(QRect(20, 640, 101, 24))
        self.btn_import_news.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser_10 = QTextBrowser(ner)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(920, 410, 211, 111))
        self.textBrowser_10.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.label_3 = QLabel(ner)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(490, 10, 81, 16))
        self.label = QLabel(ner)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 16))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_ask = QPushButton(ner)
        self.btn_import_ask.setObjectName(u"btn_import_ask")
        self.btn_import_ask.setGeometry(QRect(20, 670, 101, 24))
        self.btn_import_ask.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_kics = QPushButton(ner)
        self.btn_import_kics.setObjectName(u"btn_import_kics")
        self.btn_import_kics.setGeometry(QRect(20, 610, 101, 24))
        self.btn_import_kics.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_autotagging = QPushButton(ner)
        self.btn_autotagging.setObjectName(u"btn_autotagging")
        self.btn_autotagging.setGeometry(QRect(130, 580, 101, 24))
        self.btn_autotagging.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textBrowser = QTextBrowser(ner)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(960, 30, 171, 131))
        self.textBrowser.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.textBrowser_9 = QTextBrowser(ner)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(670, 410, 241, 111))
        self.textBrowser_9.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.textBrowser_3 = QTextBrowser(ner)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(960, 170, 171, 61))
        self.textBrowser_3.setStyleSheet(u"background-color: rgb(255, 230, 217);")
        self.label_2 = QLabel(ner)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 280, 91, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_import_court = QPushButton(ner)
        self.btn_import_court.setObjectName(u"btn_import_court")
        self.btn_import_court.setGeometry(QRect(20, 700, 101, 24))
        self.btn_import_court.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_standard = QPushButton(ner)
        self.btn_standard.setObjectName(u"btn_standard")
        self.btn_standard.setGeometry(QRect(110, 280, 101, 24))
        self.btn_standard.setStyleSheet(u"background-color: rgb(255, 251, 212)")

        self.retranslateUi(ner)

        QMetaObject.connectSlotsByName(ner)
    # setupUi

    def retranslateUi(self, ner):
        ner.setWindowTitle(QCoreApplication.translate("ner", u"ner", None))
        self.label_4.setText(QCoreApplication.translate("ner", u"\ud14d\uc2a4\ud2b8 \ubd88\ub7ec\uc624\uae30", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Date</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae30\ud0c0\ub0a0\uc9dc : dt_others&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae30\uac04 : dt_duration&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "&lt;\uc77c : dt_day&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc6d4 : dt_month&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub144 : dt_year&gt;	</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ud615\uae30 : dt_law&gt;</p></body></html>", None))
        self.btn_save.setText(QCoreApplication.translate("ner", u"\uc218\uc815\uacb0\uacfc \uc800\uc7a5", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Person</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc7ac\ud310\uc218\uc0ac\uacfc\uc815\uc0c1 \uc9c0\uc704 : ps_court&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ud53c\uc758\uc790, \ud53c\ud610\uc758\uc790 \uc774\ub984 : ps_name_accused&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ud53c\ud574\uc790 \uc774\ub984 : ps_name_victim&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ucc38\uace0\uc778 \uc774\ub984 : ps_name_witness&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub2f4\ub2f9 \uac80\uc0ac,\uacbd\ucc30 \uc774\ub984 : ps_name_justice&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub2f4\ub2f9 \ud310\uc0ac \uc774\ub984 : ps_name_judge&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub2f4\ub2f9 \ubcc0\ud638\uc0ac \uc774\ub984 : ps_name_attorney&gt;</p>\n"
"<p"
                        " align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uac10\uc815\uc778, \uc751\uae09\ucc98\uce58\uc0ac \uc774\ub984 : ps_name_appraiser&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uac00\uba85 : ps_nickname&gt;</p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Civilization</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc9c1\uc704\uc9c1\ucc45 : cv_position&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc778\uac04\uad00\uacc4 : cv_relation&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\">&lt;\uc9c1\uc5c5 : cv_occupation&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ubc95\ub960\uba85\uce6d : cv_law&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc131\ubcc4 : cv_sex&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc0ac\uce6d\uc9c1\uae09 : cv_position_fake&gt;</p></body></html>", None))
        self.btn_import_112.setText(QCoreApplication.translate("ner", u"112 \uc811\uc218\uc0ac\uc2e4", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Organization</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae30\uc5c5, \uacbd\uc81c\uad00\ub828 \ub2e8\uccb4 : og_economy&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uad50\uc721\uae30\uad00 : og_education&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc758\ub8cc\uae30\uad00 : og_medicine&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ubc95\ub960\uae30\uad00 : og_law&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc815\ubd80,\uacf5\uacf5\uae30\uad00 : og_politics&gt;	</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc74c\uc2dd\uc5c5\uccb4 : og_food&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc219\ubc15\uc5c5\uccb4 : og_hotel&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;"
                        "\ub178\ub798\ubc29 \ub4f1 \uc720\ud765\uc8fc\uc810 : og_entertainment&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ud3b8\uc758\uc810 : og_convinience&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc0ac\uce6d\ud55c \uae30\uad00 : og_fake&gt;</p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Time</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae30\ud0c0\uc2dc\uac04 : ti_others&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae30\uac04 : ti_duration&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                        "&lt;\uc2dc\uac04 : ti_hour&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ubd84 : ti_minute&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ucd08 : ti_second&gt;</p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Quantity</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub098\uc774 : qt_age&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae08\uc561 : qt_price&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px"
                        ";\">&lt;\uc804\ud654\ubc88\ud638 : qt_phone&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uacc4\uc88c\ubc88\ud638 : qt_account&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc0ac\uac74\ubc88\ud638 : qt_case&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ucc28\ub7c9\ubc88\ud638 : qt_vehicle_plate&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc8fc\ubbfc\ubc88\ud638 : qt_identity&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ubc95\ub960\uc870\ud56d : qt_law&gt;</p>\n"
"<p a"
                        "lign=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc778\ud130\ub137 \uc8fc\uc18c : qt_url&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;IP\uc8fc\uc18c : qt_ip&gt;</p></body></html>", None))
        self.btn_handtagging.setText(QCoreApplication.translate("ner", u"\uc218\ub3d9 \ud0dc\uae45\ud558\uae30", None))
        self.btn_import_news.setText(QCoreApplication.translate("ner", u"\ub124\uc774\ubc84 \ub274\uc2a4", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\ucd94\uac00\ud558\uace0 \uc2f6\uc740 \ud0dc\uadf8 \uba85\uba85\uac00\ub2a5</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ner", u"Copy Tag", None))
        self.label.setText(QCoreApplication.translate("ner", u"Random Text", None))
        self.btn_import_ask.setText(QCoreApplication.translate("ner", u"\uace0\uac1d\ub9cc\uc871, \uc124\ubb38", None))
        self.btn_import_kics.setText(QCoreApplication.translate("ner", u"KICS\ubc94\uc8c4\uc0ac\uc2e4", None))
        self.btn_autotagging.setText(QCoreApplication.translate("ner", u"\uc790\ub3d9 \ud0dc\uae45\ud558\uae30", None))
        self.textBrowser.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Location</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uae30\ud0c0\uc7a5\uc18c : lc_others&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uad6d\uac00\uba85 : lc_country&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\">&lt;\ub3c4/\uc8fc : lc_province&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uad70/\uba74/\uc74d/\ub3d9 : lc_county&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub3c4\uc2dc\uba85 : lc_city&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc12c : lc_island&gt;</p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Term</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ubc94\ud589\ub3c4\uad6c : tmc_tool&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ud53c\ud574\uc785\uc740 \ubb3c\uac74 : tmc_damaged_product&gt;</p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("ner", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Artifacts</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\uc544\ud30c\ud2b8, \uac74\ubb3c : af_building&gt;</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;\ub3c4\ub85c\uba85 : af_road&gt;</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ner", u"Tagged Text", None))
        self.btn_import_court.setText(QCoreApplication.translate("ner", u"\ud310\uacb0\ubb38", None))
        self.btn_standard.setText(QCoreApplication.translate("ner", u"\uae30\uc900\ub9cc\ub4e4\uae30", None))
    # retranslateUi

