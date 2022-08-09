import re
import sys, os
base = os.path.abspath(__file__).replace(r'\re_compiler\PS_compiler.py','')
sys.path.append(os.path.dirname(base+r'\dictionary'))

from dictionary import ps_court, relations, phishing

ps_compiler = {}
ps_compiler['ps_court_exact_stamp'] = [re.compile('%s'%('|'.join(ps_court.ps_court_dict))),
                                       re.compile('(%s)\s(\d{1,2}\,?\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                       re.compile('(%s)\s(\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                       re.compile('(%s)\s(\d{1,2}\,\s\d{1,2})'%('|'.join(ps_court.ps_court_dict)))]
#ps_court의 1번째 compiler : (피의자)
#ps_court의 2번째 compiler : (피의자)공백(1,2) -> 그룹 () () 두 요소를 하나로 합쳐야 함
#ps_court의 3번째 compiler : (피의자)공백(1) -> 그룹 () () 두 요소를 하나로 합쳐야 함
#ps_court의 4번째 compiler : (피의자)공백(1, 2) -> 그룹 () () 두 요소를 하나로 합쳐야 함
ps_compiler['ps_name_accused_total_stamp'] = [re.compile('(피의자|피고인|피고소인)\s([a-zA-Z]{1,3}\d{,1})\s?는?에?를?의?과?가?')]

#ps_name_accused의 1번째 compiler : (피의자)공백(A)는or에or를or의or과or가

ps_compiler['ps_court&name_total_stamp'] = [re.compile('%s'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s(\d{1,2}\,?\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s(\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s(\d{1,2}\,\s\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([a-zA-Z]{1,3}\d{,1})\s?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{1}\s)은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{1})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{1}[a-zA-Z]{1,2})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣\s]{1,3}\,\s[가-힣\s]{1,3}\,\s[가-힣\s]{1,3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([a-zA-Z]{1,3}\,\s[a-zA-Z]{1,3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣\s]{2,3}\,\s동\s[가-힣\s]{2,3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{1}\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{2})\s'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{3})과\s([가-힣]{3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)(\d{1})\s([가-힣]{3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)(\d{1}\))\s([가-힣]{3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{3}\,\s[가-힣]{3}\,\s[가-힣]{3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([A-Za-z]{1,3})'%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([a-zA-Z]{1,3}\s)은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('([가-힣]{1}\*\*)에\s대한\s살인'),
                                            re.compile('(%s)\s([가-힣]{1}\s[가-힣]{2})은?는?에?를?의?과?가?'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(%s)\s([가-힣]{1,3})\('%('|'.join(ps_court.ps_court_dict))),
                                            re.compile('(검사)\s([a-zA-Z가-힣]{2,3})\(기소\)\,\s([a-zA-Z가-힣]{2,3})\(공판\)'\
                                                       ),
                                            re.compile('(검사)\s([a-zA-Z가-힣]{2,3})\s(변호인)\s(변호사)\s([a-zA-Z가-힣]{2,3})\(국선\)'\
                                                       ),
                                            re.compile('(대법관)\s([가-힣]{2,3})\(재판장\)\s([가-힣]{2,3})\s([가-힣]{2,3})\s([가-힣]{2,3})'),
                                            re.compile('(변호사)\s([가-힣]{2,3}\s)\(국선\)'),
                                            re.compile('(변호인)\s(변호사)\s([a-zA-Z]{1,3})'),
                                            re.compile('(의사)\s([가-힣]{2,3})는?의?'),
                                            re.compile('(%s)인\s([a-zA-Z]{1,3})은?는?에?를?의?과?가?'\
                                                       %('|'.join(relations.relation_dict))),
                                            re.compile('(%s)\s([가-힣]{3})'%('|'.join(relations.relation_dict))),
                                            re.compile('(검사)\s작성의\s([가-힣a-zA-Z\s]{1,3}\,\s[가-힣a-zA-Z\s]{,3}'\
                                            '\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}'\
                                            '\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}'\
                                            '\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3})에\s대한\s각\s진술조서')]
#ps_court&name의 1번째 compiler : (피의자)
#ps_court&name의 2번째 compiler : (피의자)공백(1,2) -> 그룹 () () 공백기준 합침
#ps_court&name의 3번째 compiler : (피의자)공백(1) -> 그룹 () () 공백기준 합침
#ps_court&name의 4번째 compiler : (피의자)공백(1, 2) -> 그룹 () () 공백기준 합침
#ps_court&name의 5번째 compiler : (피의자)공백(A)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 6번째 compiler : (피고인)공백(김 )은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 7번째 compiler : (피고인)공백(김)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 8번째 compiler : (피고인)공백(이BB)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 9번째 compiler : (피고인)공백(함, 배 욱, 정 구)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 10번째 compiler : (피고인)공백(A, B) -> 그룹 () () 공백기준 합침
#ps court&name의 11번째 compiler : (피고인)공백(김규, 동 박@호) -> 그룹 () () 공백기준 합침
#ps court&name의 11번째 compiler : (피고인)공백(A, C, D, F)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 12번째 compiler : (피고인)공백(김00) -> 그룹 () () 공백기준 합침
#ps court&name의 13번째 compiler : (피고소인)공백(강희)공백 -> 그룹 () () 공백기준 합침
#ps court&name의 14번째 compiler : (피의자)공백(김세창)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 15번째 compiler : (피의자)공백(강희왕)과공백(여진구)는은or는or에or를or의or과or가 -> 그룹 () () () 공백&과공백 기준 합침
#ps court&name의 16번째 compiler : (피의자)(1)공백(홍길동)은or는or에or를or의or과or가 -> 그룹 () () () 특수합침
#ps court&name의 17번째 compiler : (피의자)(2괄호)공백(이재진)은or는or에or를or의or과or가 -> 그룹 () () () 특수합침
#ps court&name의 18번째 compiler : (피의자)공백(오진태, 박민혁, 양인범)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 19번째 compiler : (피해자)공백(M)( -> 그룹 () () 공백기준 합침
#ps court&name의 20번째 compiler : (피해자)공백(h )은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 21번째 compiler : (김**)에공백대한공백살인
#ps court&name의 22번째 compiler : (피해자)공백(윤 경화)은or는or에or를or의or과or가 -> 그룹 () () 공백기준 합침
#ps court&name의 23번째 compiler : (피해자)공백(박)( -> 그룹 () () 공백기준 합침
#ps court&name의 24번째 compiler : (검사)공백(김태엽)괄호기소괄호,공백(노영진)괄호공판괄호 -> 그룹 () () () 특수합침
#ps court&name의 25번째 compiler : (검사)공백(y)공백(변호인)공백(변호사)공백(z)괄호국선괄호 -> 그룹 () () () () () 특수합침
#ps court&name의 26번째 compiler : (대법관)공백(정기승)괄호재판장괄호공백(김형기)공백(김달식)공백(박우동) -> 그룹 () () () () () 특수합침
#ps court&name의 27번째 compiler : (변호사)공백(오웅 )괄호국선괄호 -> 그룹 () () 공백기준 합침
#ps court&name의 28번째 compiler : (변호인)공백(변호사)공백(B) -> 그룹 () () () 공백기준 합침
#ps court&name의 29번째 compiler : (의사)공백(황규리)는or의 -> 그룹 () () 공백기준 합침
#ps court&name의 30번째 compiler : (아버지)인공백(a)은or는or에or를or의or과or가-> 그룹 () () 특수합침
#ps court&name의 31번째 compiler : (아버지)공백(김장군)은or는or에or를or의or과or가-> 그룹 () () 공백기준 합침
#ps court&name의 32번째 compiler : (검사)공백작성의공백(e, c, a, g, 김, , 이, 노, f, 박, h)에공백대한공백각공백진술조서 -> 그룹 () () 특수합침

ps_compiler['ps_court&name_small_stamp'] = [(re.compile('(%s)'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court']),
                                            (re.compile('(%s)\s(\d{1,2}\,?\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court','ps_court']),
                                            (re.compile('(%s)\s(\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court','ps_court']),
                                            (re.compile('(%s)\s(\d{1,2}\,\s\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court','ps_court']),
                                            (re.compile('(%s)\s([a-zA-Z]{1,3}\d{,1})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{1}\s)'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{1})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{1}[a-zA-Z]{1,2})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣\s]{1,3}\,\s[가-힣\s]{1,3}\,\s[가-힣\s]{1,3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([a-zA-Z]{1,3}\,\s[a-zA-Z]{1,3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣\s]{2,3}\,\s동\s[가-힣\s]{2,3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{1}\d{1,2})'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{2})'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{3})과\s([가-힣]{3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name', 'ps_name']),
                                            (re.compile('(%s\d{1})\s([가-힣]{3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s\d{1}\))\s([가-힣]{3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{3}\,\s[가-힣]{3}\,\s[가-힣]{3})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([A-Za-z]{1,3})'%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([a-zA-Z]{1,3}\s)'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('([가-힣]{1}\*\*)에\s대한\s살인'),
                                             ['ps_name_victim']),
                                            (re.compile('(%s)\s([가-힣]{1}\s[가-힣]{2})'\
                                                       %('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{1,3})\('%('|'.join(ps_court.ps_court_dict))),
                                             ['ps_court', 'ps_name']),
                                            (re.compile('(검사)\s([a-zA-Z가-힣]{2,3})\(기소\)\,\s([a-zA-Z가-힣]{2,3})\(공판\)'\
                                                       ),
                                             ['ps_court', 'ps_name_justice','ps_name_justice']),
                                            (re.compile('(검사)\s([a-zA-Z가-힣]{2,3})\s(변호인)\s(변호사)\s([a-zA-Z가-힣]{2,3})\(국선\)'\
                                                       ),
                                             ['ps_court', 'ps_name_justice', 'ps_court', 'ps_court', 'ps_name_attorney']),
                                            (re.compile('(대법관)\s([가-힣]{2,3})\(재판장\)\s([가-힣]{2,3})\s([가-힣]{2,3})\s([가-힣]{2,3})'),
                                             ['ps_court', 'ps_name_judge','ps_name_judge','ps_name_judge','ps_name_judge']),
                                            (re.compile('(변호사)\s([가-힣]{2,3}\s)\(국선\)'),
                                             ['ps_court', 'ps_name_attorney']),
                                            (re.compile('(변호인)\s(변호사)\s([a-zA-Z]{1,3})'),
                                             ['ps_court', 'ps_court', 'ps_name_attorney']),
                                            (re.compile('(의사)\s([가-힣]{2,3})'),
                                             ['ps_court', 'ps_name_appraiser']),
                                            (re.compile('(%s)인\s([a-zA-Z]{1,3})'\
                                                       %('|'.join(relations.relation_dict))),
                                             ['cv_relation', 'ps_name']),
                                            (re.compile('(%s)\s([가-힣]{3})'%('|'.join(relations.relation_dict))),
                                             ['cv_relation', 'ps_name']),
                                            (re.compile('(검사)\s작성의\s([가-힣a-zA-Z\s]{1,3}\,\s[가-힣a-zA-Z\s]{,3}'\
                                            '\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}'\
                                            '\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}'\
                                            '\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3}\,?\s?[가-힣a-zA-Z\s]{,3})에\s대한\s각\s진술조서'),
                                             ['ps_court', 'ps_name'])]


ps_compiler['ps_voice_phising_total_stamp'] = [re.compile('(%s)\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile('(%s)\s(%s)\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['department']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile('(%s)\s(%s)\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile('(%s)\s(%s)\s([가-힣]{3})'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile("\'(%s)\s([가-힣]{3})\'를\s사칭"\
                                                          %('|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile('(%s)\s대부업체\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile('([가-힣]{3})\s(%s)을?를?\s?사칭'\
                                                          %('|'.join(phishing.phishing_dict['jobtitle']))),
                                               re.compile('(%s)\s(직원)도\s아니'%('|'.join(phishing.phishing_dict['organization']))),
                                               re.compile('(%s)\s([가-힣]{3})을?를?\s?사칭'\
                                                          %('|'.join(phishing.phishing_dict['organization']))),
                                               re.compile('\"(%s)(이다)'%('|'.join(phishing.phishing_dict['organization']))),
                                               re.compile('(%s)의\s(직원)도\s아니'%('|'.join(phishing.phishing_dict['organization'])))]

#ps_voice_phising의 1번째 compiler : (kb국민은행)공백(최명열)공백(대리) -> 그룹요소3,공백합침
#ps_voice_phising의 2번째 compiler : (예가람저축은행)공백(채권팀)공백(정수정)공백(과장) -> 그룹요소4,공백합침
#ps_voice_phising의 3번째 compiler : (아주캐피탈)공백(대출담당)공백(이병설)공백(팀장) -> 그룹요소4,공백합침
#ps_voice_phising의 4번째 compiler : (아주캐피탈)공백(직원)공백(이주희) -> 그룹요소3,공백합침
#ps_voice_phising의 5번째 compiler : 작은따옴표(검사)공백(이정호)작은따옴표를공백사칭 -> 그룹요소2,공백합침
#ps_voice_phising의 6번째 compiler : (아이앤유크레딧)공백대부업체공백(이현수)공백(과장) -> 그룹요소3,특수합침
#ps_voice_phising의 7번째 compiler : (김진수)공백(팀장)을/를공백사칭 -> 그룹요소2,공백합침
#ps_voice_phising의 8번째 compiler : (저축은행)공백(직원)도공백아니 -> 그룹요소2,공백합침
#ps_voice_phising의 9번째 compiler : (현대캐피탈)공백(김동현)을/를사칭 -> 그룹요소2,공백합침
#ps_voice_phising의 10번째 compiler : "(신한캐피탈)(이다) -> 그룹요소2,공백없이합침
#ps_voice_phising의 11번째 compiler : (저축은행)의공백(직원)도공백아니 -> 그룹요소2,특수합침

ps_compiler['ps_voice_phising_small_stamp'] = [(re.compile('(%s)\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['og_fake', 'ps_nickname', 'cv_position_fake']),
                                               (re.compile('(%s)\s(%s)\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['department']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['og_fake','og_fake','ps_nickname','cv_position_fake']),
                                               (re.compile('(%s)\s(%s)\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['og_fake','cv_position_fake','ps_nickname','cv_position_fake']),
                                               (re.compile('(%s)\s(%s)\s([가-힣]{3})'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['og_fake','cv_position_fake','ps_nickname']),
                                               (re.compile("(%s)\s([가-힣]{3})"\
                                                          %('|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['cv_position_fake','ps_nickname']),
                                               (re.compile('(%s)\s대부업체\s([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['organization']),
                                                            '|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['og_fake','ps_nickname','cv_position_fake']),
                                               (re.compile('([가-힣]{3})\s(%s)'\
                                                          %('|'.join(phishing.phishing_dict['jobtitle']))),
                                                ['ps_nickname','cv_position_fake']),
                                               (re.compile('(%s)\s(직원)'%('|'.join(phishing.phishing_dict['organization']))),
                                                ['og_fake', 'cv_position_fake']),
                                               (re.compile('(%s)\s([가-힣]{3})' \
                                                          % ('|'.join(phishing.phishing_dict['organization']))),
                                                ['og_fake', 'ps_nickname']),
                                               (re.compile('(%s)'%('|'.join(phishing.phishing_dict['organization']))),
                                                ['og_fake']),
                                               (re.compile('(%s)의\s(직원)'%('|'.join(phishing.phishing_dict['organization']))),
                                                ['og_fake', 'cv_position_fake'])
                                               ]