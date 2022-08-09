import re
import pandas as pd
import sys, os
base = os.path.abspath(__file__).replace('\extract_entity_modules\Apply_compiler.py','')
sys.path.append(os.path.dirname(base+'/re_compiler'))
sys.path.append(os.path.dirname(base+'/preprocess_functions'))

from re_compiler import DT_compiler, QT_compiler, PS_compiler, OG_compiler, LC_compiler, CV_compiler, TMC_compiler
from preprocess_functions import simple_transform
#from sample_text import *

class extract_entity:
    def __init__(self, sent_list):
        self.sent_list = sent_list
        self.found_elements = {}

    def extract_all(self, save=False):
        self.dt_others()
        self.dt_day()
        self.dt_year()
        self.dt_duration()
        self.ti_others()
        self.dt_law()
        self.qt_law()
        self.qt_age()
        self.qt_case()
        self.qt_price()
        self.qt_vehicle()
        self.qt_account()
        self.qt_phone()
        self.ps_court_name()
        self.ps_voice_phishing()
        self.og_()
        self.lc_()
        self.cv_position()
        self.cv_occupation()
        self.cv_relation()
        self.cv_law()
        self.tmc_tool()
        if save == True:
            df_result = []
            for i in range(len(self.sent_list)):
                text = self.sent_list[i]
                dt_others = self.found_elements['dt_others'][1][i]
                dt_day = self.found_elements['dt_day_total'][1][i]
                dt_year = self.found_elements['dt_year_total'][1][i]
                dt_duration = self.found_elements['dt_duration'][1][i]
                ti_others = self.found_elements['ti_others'][1][i]
                dt_law = self.found_elements['dt_law_total'][1][i]
                qt_law = self.found_elements['qt_law'][1][i]
                qt_age = self.found_elements['qt_age'][1][i]
                qt_case = self.found_elements['qt_case'][1][i]
                qt_price = self.found_elements['qt_price'][1][i]
                qt_vehicle = self.found_elements['qt_vehicle_total'][1][i]
                qt_account = self.found_elements['qt_account'][1][i]
                qt_phone = self.found_elements['qt_phone'][1][i]
                ps_court_name = self.found_elements['ps_court&name_total'][1][i]
                ps_voice_phising_total_stamp = self.found_elements['ps_voice_phising_total'][1][i]
                og_total_stamp = self.found_elements['og_total'][1][i]
                lc_total_stamp = self.found_elements['lc_total'][1][i]
                cv_position = self.found_elements['cv_position'][1][i]
                cv_occupation = self.found_elements['cv_occupation'][1][i]
                cv_relation = self.found_elements['cv_relation'][1][i]
                cv_law = self.found_elements['cv_law_total'][1][i]
                tmc_tool = self.found_elements['tmc_tool'][1][i]
                df_result.append((text, dt_others, dt_day, dt_year,dt_duration, ti_others, dt_law,
                                  qt_law, qt_age, qt_case, qt_price, qt_vehicle,qt_account, qt_phone,
                                  ps_court_name,
                                  ps_voice_phising_total_stamp, og_total_stamp,
                                  lc_total_stamp, cv_position, cv_occupation,
                                  cv_relation, cv_law,tmc_tool))

            df = pd.DataFrame(df_result)
            df.to_excel('temp_result.xls', index=False)
    def dt_others(self):
        found_elements = []
        
        #불러온 compiler들을 리스트에 담음
        use_compilers = [DT_compiler.dt_compiler['dt_others_exact_stamp'][i] for i in \
                         range(len(DT_compiler.dt_compiler['dt_others_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                #found_lists[0] : pattern1에 의해 얻어진 결과 ['2020. 1. 1.'],,,

            # found_lists[1]에서 found_lists[0]에 부분집합으로 발견된 부분은 find 결과에서 제외
            simple_transform.delete_subset(found_lists[0], found_lists[1])

            simple_transform.concat_tuple_in_list(found_lists, [3], num_of_compo=2, concat_sign=' ')

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)

            # 규칙 예외 사항 추가
            # 텍스트 마지막에 공백이 있는 경우, 규칙에 맞지 않은데 발견된 경우 제거(예 : 제10259호, 1967. 1.생)
            new_found_list = []
            for found in found_list:
                try:
                    if found[-1] == ' ':
                        found = found[:-1]
                    if len(re.findall('\d{5}', found)) == 0:
                        if len(re.findall('%s\s?생' % found, text)) == 0:
                            new_found_list.append(found)
                except:
                    pass

            found_elements.append(new_found_list)

            #print(text, new_found_list)

        self.found_elements['dt_others'] = ['exact_stamp', found_elements]

    def dt_day(self):
        found_elements = []

        # 불러온 compiler들을 리스트에 담음
        use_compilers = [DT_compiler.dt_compiler['dt_day_total_stamp'][i] for i in \
                         range(len(DT_compiler.dt_compiler['dt_day_total_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                #found_lists[0] : pattern1에 의해 얻어진 결과 ['다음날 00:00경'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)

            found_elements.append(found_list)

        self.found_elements['dt_day_total'] = ['total_stamp', found_elements]

    def dt_year(self):
        found_elements = []

        # 불러온 compiler들을 리스트에 담음
        use_compilers = [DT_compiler.dt_compiler['dt_year_total_stamp'][i] for i in \
                         range(len(DT_compiler.dt_compiler['dt_year_total_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                #found_lists[0] : pattern1에 의해 얻어진 결과 ['다음날 00:00경'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)

            found_elements.append(found_list)

        self.found_elements['dt_year_total'] = ['total_stamp', found_elements]

    def dt_duration(self):
        found_elements = []

        # 불러온 compiler들을 리스트에 담음
        use_compilers = [DT_compiler.dt_compiler['dt_duration_exact_stamp'][i] for i in \
                         range(len(DT_compiler.dt_compiler['dt_duration_exact_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                #found_lists[0] : pattern1에 의해 얻어진 결과 ['90일간'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)

            found_elements.append(found_list)

        self.found_elements['dt_duration'] = ['exact_stamp', found_elements]

    def ti_others(self):
        found_elements = []

        # 불러온 compiler들을 리스트에 담음
        use_compilers = [DT_compiler.dt_compiler['ti_others_exact_stamp'][i] for i in \
                         range(len(DT_compiler.dt_compiler['ti_others_exact_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                #found_lists[0] : pattern1에 의해 얻어진 결과 ['00:00'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)

            found_elements.append(found_list)

        self.found_elements['ti_others'] = ['exact_stamp', found_elements]

    def dt_law(self):
        found_elements = []

        # 불러온 compiler들을 리스트에 담음
        use_compilers = [DT_compiler.dt_compiler['dt_law_total_stamp'][i] for i in \
                         range(len(DT_compiler.dt_compiler['dt_law_total_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                #found_lists[0] : pattern1에 의해 얻어진 결과 ['00시간의 사회봉사'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            # 리스트 안에서 다른 요소의 부분집합이 되는 것 삭제
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)

        self.found_elements['dt_law_total'] = ['total_stamp', found_elements]

    def qt_law(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_law_exact_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_law_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 ['제21조'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = [i[:-1] if i[-1] == ' ' else i for i in found_list]
            found_list = list(set(found_list))
            # 함수를 적용해 텍스트 내의 순서대로 바꿔줌
            found_list = simple_transform.back_to_orginalorder_intxt(text, found_list)

            found_elements.append(found_list)

        self.found_elements['qt_law'] = ['exact_stamp', found_elements]

    def qt_age(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_age_exact_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_age_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 ['1991년 1월 1일 생'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            # 함수를 적용해 텍스트 내의 순서대로 바꿔줌
            found_list = simple_transform.back_to_orginalorder_intxt(text, found_list)
            found_elements.append(found_list)

        self.found_elements['qt_age'] = ['exact_stamp', found_elements]

    def qt_case(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_case_exact_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_case_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 ['2018고합1234'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_elements.append(found_list)

        self.found_elements['qt_case'] = ['exact_stamp', found_elements]

    def qt_price(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_price_exact_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_price_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 ['2018고합1234'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_elements.append(found_list)

        self.found_elements['qt_price'] = ['exact_stamp', found_elements]

    def qt_vehicle(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_vehicle&plate_total_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_vehicle&plate_total_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))

                simple_transform.concat_tuple_in_list(found_lists,[0],num_of_compo = 3, concat_sign=[' ', ' '])

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_elements.append(found_list)

        self.found_elements['qt_vehicle_total'] = ['total_stamp', found_elements]

    def qt_account(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_account_exact_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_account_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 ['2018고합1234'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_elements.append(found_list)

        self.found_elements['qt_account'] = ['exact_stamp', found_elements]

    def qt_phone(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [QT_compiler.qt_compiler['qt_phone_exact_stamp'][i] for i in \
                         range(len(QT_compiler.qt_compiler['qt_phone_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 ['2018고합1234'],,,

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_elements.append(found_list)

        self.found_elements['qt_phone'] = ['exact_stamp', found_elements]

    def ps_court(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [PS_compiler.ps_compiler['ps_court_exact_stamp'][i] for i in \
                         range(len(PS_compiler.ps_compiler['ps_court_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                # found_lists[0] : pattern1에 의해 얻어진 결과 (피의자)
                # found_lists[1] : pattern2에 의해 얻어진 결과 (공소외) (29)
                # found_lists[2] : pattern3에 의해 얻어진 결과 (피의자) (1)

                # 예외 규칙 : pattern2 [('공소외', '29')] -> ['공소외 29']로 변경
                # pattern3 [('피의자', '1')] -> ['피의자 1']로 변경
                # pattern4 [('피의자', '1, 2')] -> ['피의자 1, 2']로 변경
                simple_transform.concat_tuple_in_list(found_lists,1,concat_sign=' ')
                simple_transform.concat_tuple_in_list(found_lists,2,concat_sign=' ')
                simple_transform.concat_tuple_in_list(found_lists,3,concat_sign=' ')


            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 함수를 적용해 텍스트 내의 순서대로 바꿔줌
            found_list = simple_transform.back_to_orginalorder_intxt(text, found_list)
            found_list = list(set(found_list))

            found_elements.append(found_list)

        self.found_elements['ps_court'] = ['exact_stamp', found_elements]

    def ps_name_accused(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [PS_compiler.ps_compiler['ps_name_accused_exact_stamp'][i] for i in \
                         range(len(PS_compiler.ps_compiler['ps_name_accused_exact_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            found_elements.append(found_list)

        self.found_elements['ps_name_accused'] = ['exact_stamp', found_elements]

    def ps_court_name(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [PS_compiler.ps_compiler['ps_court&name_total_stamp'][i] for i in \
                         range(len(PS_compiler.ps_compiler['ps_court&name_total_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))

                # 예외 규칙 [('', '')] -> ['']
                simple_transform.concat_tuple_in_list(found_lists,[1,2,3,4,5,6,7,8,9,10,11,12,13,17,18,19,
                                                                   21,22,26,28,30],
                                                      num_of_compo = 2, concat_sign=' ')
                simple_transform.concat_tuple_in_list(found_lists,[14],num_of_compo = 3, concat_sign=[' ', '과 '])
                simple_transform.concat_tuple_in_list(found_lists,[15],num_of_compo = 3, concat_sign=['', ' '])
                simple_transform.concat_tuple_in_list(found_lists,[16],num_of_compo = 3, concat_sign=['', ' '])
                simple_transform.concat_tuple_in_list(found_lists,[23],num_of_compo = 3, concat_sign=[' ', '(기소), '])
                simple_transform.concat_tuple_in_list(found_lists,[24],num_of_compo = 5, concat_sign=[' ',' ',' ',' '])
                simple_transform.concat_tuple_in_list(found_lists,[25],num_of_compo = 5, concat_sign=[' ', '(재판장) ',' ',' '])
                simple_transform.concat_tuple_in_list(found_lists,[27],num_of_compo = 3, concat_sign=[' ',' '])
                simple_transform.concat_tuple_in_list(found_lists,[29],num_of_compo = 2, concat_sign='인 ')
                simple_transform.concat_tuple_in_list(found_lists,[31],num_of_compo = 2, concat_sign=' 작성의 ')

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 중복요소 제거(주의 : '피해자', '피고인' 등 필요요소도 지워짐. 우선 지워지게 냅둠)
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['ps_court&name_total'] = ['total_stamp', found_elements]

    def ps_voice_phishing(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [PS_compiler.ps_compiler['ps_voice_phising_total_stamp'][i] for i in \
                         range(len(PS_compiler.ps_compiler['ps_voice_phising_total_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))

                # 예외 규칙 [('', '')] -> ['']
                simple_transform.concat_tuple_in_list(found_lists,[4,6,7,8],num_of_compo = 2, concat_sign=' ')
                simple_transform.concat_tuple_in_list(found_lists,[9],num_of_compo = 2, concat_sign='')
                simple_transform.concat_tuple_in_list(found_lists,[10],num_of_compo = 2, concat_sign='의 ')
                simple_transform.concat_tuple_in_list(found_lists,[0,3],num_of_compo = 3, concat_sign=[' ',' '])
                simple_transform.concat_tuple_in_list(found_lists,[1,2],num_of_compo = 4, concat_sign=[' ', ' ',' '])
                simple_transform.concat_tuple_in_list(found_lists,[5],num_of_compo = 3, concat_sign=[' 대부업체 ', ' '])

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['ps_voice_phising_total'] = ['total_stamp', found_elements]

    def og_(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [OG_compiler.og_compiler['og_total_stamp'][i] for i in \
                         range(len(OG_compiler.og_compiler['og_total_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))

                simple_transform.concat_tuple_in_list(found_lists,[1,2,3],num_of_compo = 2, concat_sign='')

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['og_total'] = ['total_stamp', found_elements]

    def lc_(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [LC_compiler.lc_compiler['lc_total_stamp'][i] for i in \
                         range(len(LC_compiler.lc_compiler['lc_total_stamp']))]

        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))

                simple_transform.concat_tuple_in_list(found_lists,[7,9],num_of_compo = 2, concat_sign=' ')
                simple_transform.concat_tuple_in_list(found_lists,[4,6,8,13,14,15],num_of_compo = 3, concat_sign=[' ', ' '])
                simple_transform.concat_tuple_in_list(found_lists,[0,5],num_of_compo = 4, concat_sign=[' ', ' ',' '])
                simple_transform.concat_tuple_in_list(found_lists,[1,2,3,12],num_of_compo = 5, concat_sign=[' ', ' ',' ',' '])

            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['lc_total'] = ['total_stamp', found_elements]

    def cv_position(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [CV_compiler.cv_compiler['cv_position_exact_stamp'][i] for i in \
                         range(len(CV_compiler.cv_compiler['cv_position_exact_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['cv_position'] = ['exact_stamp', found_elements]

    def cv_occupation(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [CV_compiler.cv_compiler['cv_occupation_exact_stamp'][i] for i in \
                         range(len(CV_compiler.cv_compiler['cv_occupation_exact_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['cv_occupation'] = ['exact_stamp', found_elements]

    def cv_relation(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [CV_compiler.cv_compiler['cv_relation_exact_stamp'][i] for i in \
                         range(len(CV_compiler.cv_compiler['cv_relation_exact_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['cv_relation'] = ['exact_stamp', found_elements]

    def cv_law(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [CV_compiler.cv_compiler['cv_law_total_stamp'][i] for i in \
                         range(len(CV_compiler.cv_compiler['cv_law_total_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
                simple_transform.concat_tuple_in_list(found_lists,[1,9],num_of_compo = 2, concat_sign=' ')
                simple_transform.concat_tuple_in_list(found_lists,[2,3,4,5,6,7,8,10,11],num_of_compo = 2, concat_sign='')
            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['cv_law_total'] = ['total_stamp', found_elements]

    def tmc_tool(self):
        found_elements = []
        # 불러온 compiler들을 리스트에 담음
        use_compilers = [TMC_compiler.tmc_compiler['tmc_tool_exact_stamp'][i] for i in \
                         range(len(TMC_compiler.tmc_compiler['tmc_tool_exact_stamp']))]
        for text in self.sent_list:
            found_lists = []
            for compiler in range(len(use_compilers)):
                found_lists.append(use_compilers[compiler].findall(text))
            # found_lists에서 발견된 부분을 최종적으로 하나의 리스트로 합침
            found_list = simple_transform.make_one_list(found_lists)
            found_list = list(set(found_list))
            found_list.sort(key=len, reverse=True)

            # 리스트 안의 부분집합이 되는 중복요소 제거
            simple_transform.delete_subset_in_onelist(found_list)

            found_elements.append(found_list)
            #print(text, found_list)

        self.found_elements['tmc_tool'] = ['exact_stamp', found_elements]
