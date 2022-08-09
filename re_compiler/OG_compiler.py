import re
og_compiler = {}
og_compiler['og_total_stamp'] = [
                                 re.compile('\s([가-힣]{1,10}교도소)\s'),
                                 re.compile('\s([가-힣]{1,10}법원\s?[가-힣]{,10}지?원?)(\s|앞|에|을|의)'),
                                re.compile('\s([가-힣a-zA-Z\s]{1,10}병원)(\s|에서)'),
                                re.compile('\s([가-힣]{1,10}법원)(\s|앞|에|을|의)')]

#1번 컴파일러 : 공백(군산교도소)공백
#2번 컴파일러 : 공백(대전지방법원 천안지원)(앞or을or에서or에or의) -> ()()공백없이 합침
#3번 컴파일러 : 공백(d병원)(에서) -> ()()공백없이 합침
#4번 컴파일러 : 공백(대전지방법원)(에서)-> ()()공백없이 합침

og_compiler['og_small_stamp'] = [
    (re.compile('([가-힣]{1,10}교도소)'),
     ['og_politics']),
    (re.compile('([가-힣]{1,10}법원\s?[가-힣]{,10}지원)'),
     ['og_law']),
    (re.compile('([가-힣a-zA-Z\s]{1,10}병원)'),
     ['og_medicine']),
    (re.compile('([가-힣]{1,10}법원)'),
     ['og_law'])]