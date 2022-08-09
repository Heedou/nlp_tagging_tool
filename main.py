import sys
import random
import time
import re
import os

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
from PySide6.QtCore import QTimer

from taskname import Ui_MainWindow

from dialog_ner import Ui_ner
from dialog_keyword import Ui_keyword
from dialog_attribute import Ui_attribute
from dialog_crtype import Ui_crtype
from dialog_provision import Ui_provision

from extract_entity_modules.Apply_compiler import *
from extract_entity_modules.Generate_tag import *

class provision(QDialog):

    def __init__(self, parent):
        super(provision, self).__init__(parent)
        self.ui = Ui_provision()
        self.ui.setupUi(self)
        self.show()
        self.save_type = ''

        self.ui.btn_import_112.clicked.connect(self.send_112)

        self.ui.btn_import_court.clicked.connect(self.send_court)

        self.ui.btn_import_news.clicked.connect(self.send_news)

        self.ui.btn_save.clicked.connect(lambda : self.save(self.save_type))

    def send_news(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'news' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'news'

    def send_court(self):

        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'lawinformation' in file or 'lawnb' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'court'

    def send_112(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        files_112 = []

        for file in files:
            if 'txt' in file and '112_single' in file:
                files_112.append(file)
        #랜덤하게 파일 하나 선택
        selected_file = files_112[random.randint(0, len(files_112))]
        lines = []
        file_path = single_sentence_path+'/'+selected_file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines += f.readlines()

        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = '112'

    def save(self, save_type):
        tagged_text = self.ui.edit_law.toPlainText()
        #생성하는 현재 시분초
        generated_time = time.strftime('%X', time.localtime(time.time()))
        generated_time = re.sub(':', '', generated_time)
        #생성하는 현재 날짜
        generated_time_ = time.strftime('%x', time.localtime(time.time()))
        generated_time_ = re.sub('\/', '', generated_time_)
        with open('./../../Traindata/NER_dataset/%s_%s.txt'%(save_type, generated_time_+'_'+generated_time),'w', encoding='utf-8') as f:
            f.write(tagged_text)

class crtype(QDialog):

    def __init__(self, parent):
        super(crtype, self).__init__(parent)
        self.ui = Ui_crtype()
        self.ui.setupUi(self)
        self.show()
        self.save_type = ''

        self.ui.btn_import_112.clicked.connect(self.send_112)

        self.ui.btn_import_court.clicked.connect(self.send_court)

        self.ui.btn_import_news.clicked.connect(self.send_news)

        self.ui.btn_save.clicked.connect(lambda : self.save(self.save_type))

    def send_news(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'news' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'news'

    def send_court(self):

        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'lawinformation' in file or 'lawnb' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'court'

    def send_112(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        files_112 = []

        for file in files:
            if 'txt' in file and '112_single' in file:
                files_112.append(file)
        #랜덤하게 파일 하나 선택
        selected_file = files_112[random.randint(0, len(files_112))]
        lines = []
        file_path = single_sentence_path+'/'+selected_file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines += f.readlines()

        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = '112'

    def save(self, save_type):
        tagged_text = self.ui.edit_crtype.toPlainText()
        #생성하는 현재 시분초
        generated_time = time.strftime('%X', time.localtime(time.time()))
        generated_time = re.sub(':', '', generated_time)
        #생성하는 현재 날짜
        generated_time_ = time.strftime('%x', time.localtime(time.time()))
        generated_time_ = re.sub('\/', '', generated_time_)
        with open('./../../Traindata/NER_dataset/%s_%s.txt'%(save_type, generated_time_+'_'+generated_time),'w', encoding='utf-8') as f:
            f.write(tagged_text)

class attribute(QDialog):

    def __init__(self, parent):
        super(attribute, self).__init__(parent)
        self.ui = Ui_attribute()
        self.ui.setupUi(self)
        self.show()
        self.save_type = ''

        self.ui.btn_import_112.clicked.connect(self.send_112)

        self.ui.btn_import_court.clicked.connect(self.send_court)

        self.ui.btn_import_news.clicked.connect(self.send_news)

        self.ui.btn_save.clicked.connect(lambda : self.save(self.save_type))

    def send_news(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'news' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'news'

    def send_court(self):

        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'lawinformation' in file or 'lawnb' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'court'

    def send_112(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        files_112 = []

        for file in files:
            if 'txt' in file and '112_single' in file:
                files_112.append(file)
        #랜덤하게 파일 하나 선택
        selected_file = files_112[random.randint(0, len(files_112))]
        lines = []
        file_path = single_sentence_path+'/'+selected_file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines += f.readlines()

        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = '112'

    def save(self, save_type):
        tagged_text = self.ui.edit_attribute.toPlainText()
        #생성하는 현재 시분초
        generated_time = time.strftime('%X', time.localtime(time.time()))
        generated_time = re.sub(':', '', generated_time)
        #생성하는 현재 날짜
        generated_time_ = time.strftime('%x', time.localtime(time.time()))
        generated_time_ = re.sub('\/', '', generated_time_)
        with open('./../../Traindata/NER_dataset/%s_%s.txt'%(save_type, generated_time_+'_'+generated_time),'w', encoding='utf-8') as f:
            f.write(tagged_text)


class keyword(QDialog):

    def __init__(self, parent):
        super(keyword, self).__init__(parent)
        self.ui = Ui_keyword()
        self.ui.setupUi(self)
        self.show()
        self.save_type = ''

        self.ui.btn_import_112.clicked.connect(self.send_112)

        self.ui.btn_import_court.clicked.connect(self.send_court)

        self.ui.btn_import_news.clicked.connect(self.send_news)

        self.ui.btn_import_112voice.clicked.connect(self.send_112voice)

        self.ui.btn_save.clicked.connect(lambda : self.save(self.save_type))

    def send_112voice(self):
        single_sentence_path = './../../Preprocessed/Singlesentence_onlyvoice_112'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'voice' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        lines = ''.join(lines)
        lines = lines.split('*******************************')
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.ui.edit_keyword.setText(self.raw_text)
        self.save_type = '112voice'

    def send_news(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'news' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.ui.edit_keyword.setText(self.raw_text)
        self.save_type = 'news'

    def send_court(self):

        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'lawinformation' in file or 'lawnb' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.ui.edit_keyword.setText(self.raw_text)
        self.save_type = 'court'

    def send_112(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        files_112 = []

        for file in files:
            if 'txt' in file and '112_single' in file:
                files_112.append(file)
        #랜덤하게 파일 하나 선택
        selected_file = files_112[random.randint(0, len(files_112))]
        lines = []
        file_path = single_sentence_path+'/'+selected_file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines += f.readlines()

        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.ui.edit_keyword.setText(self.raw_text)
        self.save_type = '112'

    def save(self, save_type):
        tagged_text = self.ui.edit_keyword.toPlainText()
        #생성하는 현재 시분초
        generated_time = time.strftime('%X', time.localtime(time.time()))
        generated_time = re.sub(':', '', generated_time)
        #생성하는 현재 날짜
        generated_time_ = time.strftime('%x', time.localtime(time.time()))
        generated_time_ = re.sub('\/', '', generated_time_)
        with open('./../../Traindata/Keyword_dataset/%s_%s.txt'%(save_type, generated_time_+'_'+generated_time),'w', encoding='utf-8') as f:
            f.write(tagged_text)


class ner(QDialog):

    def __init__(self, parent):
        super(ner, self).__init__(parent)
        self.ui = Ui_ner()
        self.ui.setupUi(self)
        self.show()
        self.save_type = ''

        self.ui.btn_import_112.clicked.connect(self.send_112)

        self.ui.btn_import_court.clicked.connect(self.send_court)

        self.ui.btn_import_news.clicked.connect(self.send_news)


        self.ui.btn_autotagging.clicked.connect(self.autotagging)

        self.ui.btn_save.clicked.connect(lambda : self.save(self.save_type))

    def send_news(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'news' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'news'

    def send_court(self):

        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        lines = []
        for file in files:
            if 'txt' in file and 'lawinformation' in file or 'lawnb' in file:
                file_path = single_sentence_path+'/'+file
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines += f.readlines()
        #lines = [i for i in lines if not '==' in lines]
        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = 'court'

    def send_112(self):
        single_sentence_path = './../../Preprocessed/Singlesentence'
        files = os.listdir(single_sentence_path)
        files_112 = []

        for file in files:
            if 'txt' in file and '112_single' in file:
                files_112.append(file)
        #랜덤하게 파일 하나 선택
        selected_file = files_112[random.randint(0, len(files_112))]
        lines = []
        file_path = single_sentence_path+'/'+selected_file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines += f.readlines()

        self.raw_text = lines[random.randint(0, len(lines))]
        self.ui.edit_random.setText(self.raw_text)
        self.save_type = '112'

    def autotagging(self):

        raw_texts_list = []
        raw_texts_list.append(self.raw_text)

        step1 = extract_entity(raw_texts_list)
        step1.extract_all(save=False)
        step2 = generate_tag(step1)
        step2.all_stamp()
        step2.small_stamp2()
        step2.follow_up()

        self.ui.edit_tagging.setText(step2.tagged_texts[0])

    def save(self, save_type):
        tagged_text = self.ui.edit_tagging.toPlainText()
        #생성하는 현재 시분초
        generated_time = time.strftime('%X', time.localtime(time.time()))
        generated_time = re.sub(':', '', generated_time)
        #생성하는 현재 날짜
        generated_time_ = time.strftime('%x', time.localtime(time.time()))
        generated_time_ = re.sub('\/', '', generated_time_)
        with open('./../../Traindata/NER_dataset/%s_%s.txt'%(save_type, generated_time_+'_'+generated_time),'w', encoding='utf-8') as f:
            f.write(tagged_text)


class MainWindow_taskname(QMainWindow):

    def __init__(self):
        super(MainWindow_taskname, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_ner.clicked.connect(self.ner)
        self.ui.btn_keyword.clicked.connect(self.keyword)
        self.ui.btn_sentence.clicked.connect(self.attribute)
        self.ui.btn_crtype.clicked.connect(self.crtype)
        self.ui.btn_legal.clicked.connect(self.provision)

    def ner(self):
        ner(self)

    def keyword(self):
        keyword(self)

    def attribute(self):
        attribute(self)

    def crtype(self):
        crtype(self)

    def provision(self):
        provision(self)

if __name__ == '__main__':
    app = QApplication()

    window = MainWindow_taskname()
    window.show()

    sys.exit(app.exec_())