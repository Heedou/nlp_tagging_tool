import re
from dictionary import vehicles
qt_compiler = {}

qt_compiler['qt_law_exact_stamp'] = [re.compile('법\s(제\d{1,3}조) 전단'),
                                     re.compile('(제\d{,3}조의?\s?제?\d{,2}항?\s?제?\d{,2}호?)')]
#qt_law의 1번째 compiler : 법 (제21조) 전단
#qt_law의 2번째 compiler : (제1조 제2항 제3호)

qt_compiler['qt_age_exact_stamp'] = [re.compile('\d{2,4}\.?년?\s?\d{,2}\.?월?\s?\d{,2}\.?일?\s?생'),
                                     re.compile('\d{1,2}세'),
                                     re.compile('(\d{1,2})\s?~\s?\d{1,2}세')]
#qt_age의 1번째 compiler : 1991년 1월 1일 생
#qt_age의 2번째 compiler : 24세
#qt_age의 3번째 compiler : 12~13세

qt_compiler['qt_case_exact_stamp'] = [re.compile('\d{4}고단?합?\d{3,4}'),
                                      re.compile('\d{4}도\d{3,4}')]
#qt_case의 1번째 compiler : 2018고합1234
#qt_case의 2번째 compiler : 2018도1234

qt_compiler['qt_price_exact_stamp'] = [re.compile('\d{1,3}\,?\d{1,3}\,?\d{,3}원'),
                                       re.compile('\d{1,3}억\s?\d{,3}\,?\d{,3}만?\s?원'),
                                       re.compile('\d{1,3}\,\d{2,}만\s?원'),
                                       re.compile('\d{1,3}만\s?원'),
                                       re.compile('\d{1,2}만\d{1,3}\,\d{1,3}원')]
#qt_price의 1번째 compiler : 100,000,000원
#qt_price의 1번째 compiler : 1억 2000만 원
#qt_price의 3번째 compiler : 2,800만원
#qt_price의 4번째 compiler : 800만 원
#qt_price의 5번째 compiler : 4만1,300원

qt_compiler['qt_vehicle&plate_total_stamp'] = [re.compile('(\d{2,3}[가-힣]{1,2}\d{4}호?)\s(%s)\s(승용차)'\
                                                          %('|'.join(vehicles.vehicle_dict)))]
#1번째 컴파일러 : (01보7334호)공백(소나타)공백(승용차) -> () () () 공백합침
#2번째 컴파일러 : (T)공백(엑센트)공백(승용차)

qt_compiler['qt_vehicle&plate_small_stamp'] = [(re.compile('(\d{2,3}[가-힣]{1,2}\d{4}호?)\s(%s)\s승용차'\
                                                          %('|'.join(vehicles.vehicle_dict))),
                                                ['qt_vehicle_plate','af_transport'])]

qt_compiler['qt_account_exact_stamp'] = [re.compile('(\d{10,30})계좌로'),
                                         re.compile('은행\s{,2}([\d\-]{10,30})\s{,2}계좌'),
                                         re.compile('농협\s?([\d\-]{10,30})\s{,2}계좌'),
                                         re.compile('은행\s?계좌([\d\-]{10,30})로'),
                                         re.compile('계좌\(([\d\-]{10,30})\)로'),
                                         re.compile('계좌\(([\d\-]{10,30})\)에서'),
                                         re.compile('은행\s?\(([\d\-]{10,30})\)계좌로')]
#1번째 컴파일러 : (123123123123)계좌로
#2번째 컴파일러 : 은행공백(123123123)공백계좌
#3번째 컴파일러 : 농협(123123123)계좌
#4번째 컴파일러 : 은행공백계좌(123123123)로
#5번째 컴파일러 : 계좌괄호(123123)괄호로

qt_compiler['qt_phone_exact_stamp'] = [re.compile('발신번호\s?(010[\d\-]{5,10})로'),
                                       re.compile("전화번호\s\'?(010[\d\-]{5,10})\'"),
                                       re.compile("\'?(010[\d\-]{5,10})\'?번으로"),
                                       re.compile('\s(010[\d\-]{5,10})을')]
#1번째 컴파일러 : 발신번호(010123123)로
#2번째 컴파일러 : 전화번호 '010-1234-1234'으로
#3번째 컴파일러 : '010-1234-1234'번으로
#4번째 컴파일러 : 공백(010-1234-1234)을공백
