
import re
import sys, os
base = os.path.abspath(__file__).replace('\extract_entity_modules\Generate_tag.py','')
sys.path.append(os.path.dirname(base+'/re_compiler'))
sys.path.append(os.path.dirname(base+'/preprocess_functions'))

from re_compiler import PS_compiler, CV_compiler, DT_compiler, LC_compiler, OG_compiler, QT_compiler
from preprocess_functions import simple_transform, tagging_function

class generate_tag:
    def __init__(self,extracted_entity):
        self.rawtexts = extracted_entity.sent_list
        self.texts = [i for i in self.rawtexts]
        self.entities = extracted_entity.found_elements
        self.tagged_texts = []

    def all_stamp(self):
        for i in range(len(self.rawtexts)):
            temp_text = self.rawtexts[i]
            temp_text = re.sub('<', '', temp_text)
            temp_text = re.sub('>', '', temp_text)
            #temp_text : '피의자는 2019.1.1경 피의자였다.'

            all_list = []
            for k in self.entities.keys():
                for en in self.entities[k][1][i]:
                    all_list += [(en, k)]
            # all_list : [('피의자',PS), ('2019.1.1',DT)]

            all_list = simple_transform.delete_subset_in_onelist2(all_list)

            all_list.sort(key=lambda x: len(x[0]), reverse=True)
            # all_list : [('2019.1.1',DT), ('피의자',PS)]


            or_list = simple_transform.back_to_orginalorder_intxt(temp_text, [i[0] for i in all_list])
            # or_list : ['피의자', '2019.1.1']
            #print(all_list,or_list)


            self.texts[i] = tagging_function.split_sub_concat(temp_text, 
                                                              found = [i[0] for i in all_list],
                                                              tag = [i[1] for i in all_list],
                                                              or_list = or_list,
                                                              reor_list = [i[0] for i in all_list])
    def small_stamp(self):
        for i in range(len(self.texts)):
            temp_text = self.texts[i]
            temp_temp = temp_text.split('<')
            result = []
            for i in temp_temp:
                result += i.split('>')
            result = [i for i in result if len(re.findall(' : [a-z]{1,}', i)) > 0]
            result = ['<%s>' % i for i in result if 'total' in i]
            for tag in result:
                if 'ps_court&name_total' in tag:
                    tag_ps_court = re.sub('<', '', tag)
                    for i in range(len(PS_compiler.ps_compiler['ps_court&name_small_stamp'])):
                        compiler = PS_compiler.ps_compiler['ps_court&name_small_stamp'][i][0]
                        if len(compiler.findall(tag_ps_court))>0:
                            found_en = []
                            for com in compiler.findall(tag_ps_court):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass

                                else:
                                    found_en.append(com)
                            tag_ps_court2 = tag_ps_court
                            for f, t in zip(found_en,
                                            PS_compiler.ps_compiler['ps_court&name_small_stamp'][i][1]):

                                tag_ps_court2 = re.sub(f, '<%s : %s>'%(f,t), tag_ps_court2)
                                #print(tag2)
                    try:
                        tag_ps_court2 = re.sub(' : ps_court&name_total>', '', tag_ps_court2)
                        tag_ps_court2 = re.sub(': ps_court&name_total>', '', tag_ps_court2)
                        #print(tag2)
                    except:
                        pass
                    try:
                        temp_text = re.sub(tag_ps_court, tag_ps_court2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'ps_voice_phising_total' in tag:
                    tag_ps_voice = re.sub('<', '', tag)
                    for i in range(len(PS_compiler.ps_compiler['ps_voice_phising_small_stamp'])):
                        compiler = PS_compiler.ps_compiler['ps_voice_phising_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag_ps_voice2 = tag_ps_voice
                            for f, t in zip(found_en,
                                            PS_compiler.ps_compiler['ps_voice_phising_small_stamp'][i][1]):

                                tag_ps_voice2 = re.sub(f, '<%s : %s>'%(f,t), tag_ps_voice2)
                                #print(tag2)
                    try:
                        tag_ps_voice2 = re.sub(' : ps_voice_phising_total>', '', tag_ps_voice2)
                        tag_ps_voice2 = re.sub(': ps_voice_phising_total>', '', tag_ps_voice2)
                        #print(tag2)
                    except:
                        pass
                    try:
                        temp_text = re.sub(tag_ps_voice, tag_ps_voice2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'cv_law_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(CV_compiler.cv_compiler['cv_law_small_stamp'])):
                        compiler = CV_compiler.cv_compiler['cv_law_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            CV_compiler.cv_compiler['cv_law_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    tag2 = re.sub(' : cv_law_total>', '', tag2)
                    tag2 = re.sub(': cv_law_total>', '', tag2)
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'dt_day_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(DT_compiler.dt_compiler['dt_day_small_stamp'])):
                        compiler = DT_compiler.dt_compiler['dt_day_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            DT_compiler.dt_compiler['dt_day_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    tag2 = re.sub(' : dt_day_total>', '', tag2)
                    tag2 = re.sub(': dt_day_total>', '', tag2)
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'dt_year_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(DT_compiler.dt_compiler['dt_year_small_stamp'])):
                        compiler = DT_compiler.dt_compiler['dt_year_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            DT_compiler.dt_compiler['dt_year_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    tag2 = re.sub(' : dt_year_total>', '', tag2)
                    tag2 = re.sub(': dt_year_total>', '', tag2)
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'dt_law_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(DT_compiler.dt_compiler['dt_law_small_stamp'])):
                        compiler = DT_compiler.dt_compiler['dt_law_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            DT_compiler.dt_compiler['dt_law_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    tag2 = re.sub(' : dt_law_total>', '', tag2)
                    tag2 = re.sub(': dt_law_total>', '', tag2)
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'lc_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(LC_compiler.lc_compiler['lc_small_stamp'])):
                        compiler = LC_compiler.lc_compiler['lc_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            LC_compiler.lc_compiler['lc_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    try:
                        tag2 = re.sub(' : lc_total>', '', tag2)
                        tag2 = re.sub(': lc_total>', '', tag2)
                    except:
                        pass
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'og_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(OG_compiler.og_compiler['og_small_stamp'])):
                        compiler = OG_compiler.og_compiler['og_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            OG_compiler.og_compiler['og_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    tag2 = re.sub(' : og_total>', '', tag2)
                    tag2 = re.sub(': og_total>', '', tag2)
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

                if 'qt_vehicle_total' in tag:
                    tag = re.sub('<', '', tag)
                    for i in range(len(QT_compiler.qt_compiler['qt_vehicle&plate_small_stamp'])):
                        compiler = QT_compiler.qt_compiler['qt_vehicle&plate_small_stamp'][i][0]
                        if len(compiler.findall(tag))>0:
                            found_en = []
                            for com in compiler.findall(tag):
                                if type(com) == tuple:
                                    found_en.append(com[0])
                                    found_en.append(com[1])
                                    try:
                                        found_en.append(com[2])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[3])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[4])
                                    except:
                                        pass
                                    try:
                                        found_en.append(com[5])
                                    except:
                                        pass
                                else:
                                    found_en.append(com)
                            tag2 = tag
                            for f, t in zip(found_en,
                                            QT_compiler.qt_compiler['qt_vehicle&plate_small_stamp'][i][1]):

                                tag2 = re.sub(f, '<%s : %s>'%(f,t), tag2)
                                #print(tag2)
                    tag2 = re.sub(' : qt_vehicle_total>', '', tag2)
                    tag2 = re.sub(': qt_vehicle_total>', '', tag2)
                    #print(tag2)
                    try:
                        temp_text = re.sub(tag, tag2, temp_text)
                        temp_text = re.sub('<<', '<', temp_text)
                    except:
                        pass

            self.tagged_texts.append(temp_text)
    def small_stamp2(self):
        for i in range(len(self.texts)):
            temp_text = self.texts[i]
            temp_temp = temp_text.split('<')
            result = []
            for i in temp_temp:
                result += i.split('>')
            result = [i for i in result if len(re.findall(' : [a-z]{1,}', i)) > 0]
            result = ['<%s>' % i for i in result if 'total' in i]
            for tag in result:
                temp_text = tagging_function.make_small_tag(total_tag_list=['ps_court&name_total', PS_compiler.ps_compiler['ps_court&name_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['ps_voice_phising_total', PS_compiler.ps_compiler['ps_voice_phising_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['cv_law_total', CV_compiler.cv_compiler['cv_law_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['dt_day_total', DT_compiler.dt_compiler['dt_day_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['dt_year_total', DT_compiler.dt_compiler['dt_year_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['dt_law_total', DT_compiler.dt_compiler['dt_law_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['lc_total', LC_compiler.lc_compiler['lc_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['og_total', OG_compiler.og_compiler['og_small_stamp']]
                                                ,tag = tag, text = temp_text)
                temp_text = tagging_function.make_small_tag(total_tag_list=['qt_vehicle_total', QT_compiler.qt_compiler['qt_vehicle&plate_small_stamp']]
                                                ,tag = tag, text = temp_text)

            self.tagged_texts.append(temp_text)

    def follow_up(self):

        for i in range(len(self.tagged_texts)):
            # 수정필요 사항 1 피해자 태깅 안됨
            self.tagged_texts[i] = re.sub(' 피해자를 ', ' <피해자 : ps_court>를 ', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub(' 피해자가 ', ' <피해자 : ps_court>가 ', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub(' 피고인들의 ', ' <피고인들 : ps_court>의 ', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub(' 피해자의 ', ' <피해자 : ps_court>의 ', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub(' 피해자에게 ', ' <피해자 : ps_court>에게 ', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub(' 피해자에 ', ' <피해자 : ps_court>에 ', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub(' 피해자와 ', ' <피해자 : ps_court>와 ', self.tagged_texts[i])

            # 수정필요 사항 2 <피의자 : ps_court> <성명불 : ps_name>상
            self.tagged_texts[i] = re.sub('<피의자 : ps_court> <성명불 : ps_name>상',
                                          '<피의자 : ps_court> 성명불상', self.tagged_texts[i])

            # 수정필요 사항 3 <피의자 : ps_court> <명 : ps_name>의
            self.tagged_texts[i] = re.sub('<피의자 : ps_court> <명 : ps_name>의',
                                          '<피의자 : ps_court> 명의', self.tagged_texts[i])
            self.tagged_texts[i] = re.sub('<피해자 : ps_court> <명 : ps_name>의',
                                          '<피해자 : ps_court> 명의', self.tagged_texts[i])

            # 수정필요 사항 4 <직원을 : ps_nickname>
            self.tagged_texts[i] = re.sub('<직원을 : ps_nickname>',
                                          '<직원 : cv_position_fake>을', self.tagged_texts[i])



