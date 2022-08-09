import re
dt_compiler = {}

dt_compiler['dt_others_exact_stamp'] = [re.compile('\d{4}[\.년]?\s?\d{1,2}[\.월]?\s?\d{,2}[\.일]?'),
                                        re.compile('\d{1,2}\.{1}\s?\d{1,2}\.{1}'),
                                        re.compile('같은\s?[해달]{1}\s?\d{1,2}\.\s?\d{,2}\.?'),
                                        re.compile('(\d{4}\.?년?)\s(봄|여름|가을|겨울)경')]
#dt_others의 1번째 compiler : (2020. 1. 1.)
#dt_others의 2번째 compiler : (1. 3.) 1번째 compiler와 겹치는 부분 제외 필요
#dt_others의 3번째 compiler : (같은 해 1.1.경), (같은 달 7.경)
#dt_others의 4번째 compiler : (2018.)공백(겨울)경 -> () () 공백합침

dt_compiler['dt_day_total_stamp'] = [re.compile('다음\s?날[ㄱ-힣]{,1}\s?\d{1,2}[:\.]\s{,1}\d{1,2}'),
                                     re.compile('같은\s?날[ㄱ-힣]{,1}\s?\d{1,2}[:\.]\s{,1}\d{1,2}'),
                                     re.compile('당일[ㄱ-힣]{,1}\s?\d{1,2}[:\.]\s{,1}\d{1,2}')]
#dt_day 1번째 compiler : (다음날 00:00경)
#dt_day 2번째 compiler : (같은날 00:00경)
#dt_day 3번째 compiler : (당일 00:00경)

dt_compiler['dt_day_small_stamp'] = [(re.compile('(다음\s?날)[ㄱ-힣]{,1}\s?(\d{1,2}[:\.]\s{,1}\d{1,2})'),
                                      ['dt_day', 'ti_others']),
                                     (re.compile('(같은\s?날)[ㄱ-힣]{,1}\s?(\d{1,2}[:\.]\s{,1}\d{1,2})'),
                                      ['dt_day', 'ti_others']),
                                     (re.compile('(당일)[ㄱ-힣]{,1}\s?(\d{1,2}[:\.]\s{,1}\d{1,2})'),
                                      ['dt_day','ti_others'])]

dt_compiler['dt_year_total_stamp'] = [re.compile('(\d{4}\.경부터)')]
#dt_year 1컴파일러 :  1998.경부터
dt_compiler['dt_year_small_stamp'] = [(re.compile('(\d{4}\.)경부터'),
                                       ['dt_year'])]

dt_compiler['dt_duration_exact_stamp'] = [re.compile('\d{1,3}일간')]
#dt_duration 1번째 compiler : (90일간)

dt_compiler['ti_others_exact_stamp'] = [re.compile('(\d{1,2}\s{,1}:\s{,1}\d{1,2})경'),
                                        re.compile('\s(\d{1,2}:\d{1,2})부터\s\d{1,2}:\d{1,2}\s'),
                                        re.compile('\s\d{1,2}:\d{1,2}부터\s(\d{1,2}:\d{1,2})\s')]
#ti_others 1번째 compiler : (00:00)경
#ti_others 2번째 compiler : 공백(02:00)부터공백06:05공백


dt_compiler['dt_law_total_stamp'] = [re.compile('\d{1,3}시간[ㄱ-힣\s]{,3}사회봉사'),
                                     re.compile('징역\s?\d{1,2}[년|월|개월]?\s?\d{,2}월?'),
                                     re.compile('집행유예\s?\d{1,2}[년월]?\s?\d{,2}월?'),
                                     re.compile('징역\s?\d{1,2}[년|월|개월]?\s?\d{,2}월?\s?~\s?\d{1,2}[년|월|개월]?\d{,2}개?월?'),
                                     re.compile('\d{1,2}년?개?월?[ㄱ-힣\s]{,3}보호관찰'),
                                     re.compile('장?단?기[\s\,]{1,2}\d{1,2}년?개?월?')]
#dt_law 1번째 compiler : (00시간의 사회봉사)
#dt_law 2번째 compiler : (징역 1년 6월)
#dt_law 3번째 compiler : (집행유예 1년 6월)
#dt_law 4번째 compiler : (징역 1년 6월 ~ 2년 4월)
#dt_law 5번째 compiler : (1년 간 보호관찰)
#dt_law 6번째 compiler : (장기 6년)

dt_compiler['dt_law_small_stamp'] = [(re.compile('(\d{1,3}시간)[ㄱ-힣\s]{,3}(사회봉사)'),
                                      ['dt_law','cv_law']),
                                     (re.compile('(징역)\s?(\d{1,2}[년|월|개월]?\s?\d{,2}월?)'),
                                      ['cv_law','dt_law']),
                                     (re.compile('(집행유예)\s?(\d{1,2}[년월]?\s?\d{,2}월?)'),
                                      ['cv_law', 'dt_law']),
                                     (re.compile('(징역)\s?(\d{1,2}[년|월|개월]?\s?\d{,2}월?\s?~\s?\d{1,2}[년|월|개월]?\d{,2}개?월?)'),
                                      ['cv_law', 'dt_law']),
                                     (re.compile('(\d{1,2}년?개?월?)[ㄱ-힣\s]{,3}(보호관찰)'),
                                      ['dt_law','cv_law']),
                                     (re.compile('장?단?기[\s\,]{1,2}(\d{1,2}년?개?월?)'),
                                      ['dt_law'])]


dt_compiler['dt_law_exact_stamp'] = [re.compile('\d{1,3}시간[ㄱ-힣\s]{,3}사회봉사'),
                                     re.compile('징역\s?\d{1,2}[년|월|개월]?\s?\d{,2}월?'),
                                     re.compile('집행유예\s?\d{1,2}[년월]?\s?\d{,2}월?'),
                                     re.compile('징역\s?\d{1,2}[년|월|개월]?\s?\d{,2}월?\s?~\s?\d{1,2}[년|월|개월]?\d{,2}개?월?'),
                                     re.compile('\d{1,2}년?개?월?[ㄱ-힣\s]{,3}보호관찰'),
                                     re.compile('장?단?기[\s\,]{1,2}\d{1,2}년?개?월?')]
#dt_law 1번째 compiler : (00시간)의 사회봉사
#dt_law 2번째 compiler : 징역 (1년 6월)
#dt_law 3번째 compiler : 집행유예 (1년 6월)
#dt_law 4번째 compiler : 징역 (1년 6월) ~ (2년 4월)
#dt_law 5번째 compiler : (1년) 간 보호관찰
#dt_law 6번째 compiler : 장기 (6년)