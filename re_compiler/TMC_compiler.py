import re
import sys, os
base = os.path.abspath(__file__).replace(r'\re_compiler\TMC_compiler.py','')
sys.path.append(os.path.dirname(base+r'\dictionary'))

from dictionary import tools

tmc_compiler = {}

tmc_compiler['tmc_tool_exact_stamp'] = [re.compile('\s(칼)날이\s'),
                                        re.compile('\s([가-힣]{2,5})\(전체\s길이'),
                                        re.compile('미리\s준비하고\s있던\s([가-힣]{1,5})로'),
                                        re.compile('\s(%s)\('%('|'.join(tools.tool_dict['crime_tool']))),
                                        re.compile('\s(%s)를\s들고'%('|'.join(tools.tool_dict['crime_tool'])))]
#tmc_tool의 1번째 compiler : 공백(칼)날이공백
#tmc_tool의 2번째 compiler : 공백(식칼)괄호전체공백길이
#tmc_tool의 3번째 compiler : 미리공백준비하고공백있던공백(커터칼)로
#tmc_tool의 4번째 compiler : 공백(톱)괄호
#tmc_tool의 4번째 compiler : 공백(손도끼)를공백들고