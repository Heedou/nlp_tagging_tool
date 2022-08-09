import re
import sys, os
base = os.path.abspath(__file__).replace(r'\re_compiler\CV_compiler.py','')
sys.path.append(os.path.dirname(base+r'\dictionary'))

from dictionary import positions, laws, occupations, relations

cv_compiler = {}

cv_compiler['cv_position_exact_stamp'] = [re.compile('\s(%s)이다'%('|'.join(positions.position_dict))),
                                          re.compile('\s(%s)으로\s'%('|'.join(positions.position_dict)))]
#1번째 컴파일러 : 공백(사장)이다
#2번째 컴파일러 : 공백(팀장)으로공백

cv_compiler['cv_occupation_exact_stamp'] = [re.compile('\s(%s)이다'%('|'.join(occupations.occupation_dict))),
                                            re.compile('\s(%s)로\s재직'%('|'.join(occupations.occupation_dict))),
                                            re.compile('\s(%s)을\s한다'%('|'.join(occupations.occupation_dict))),
                                            re.compile('\s(%s)가\s'%('|'.join(occupations.occupation_dict)))]
#1번째 컴파일러 : 공백(자영업자)이다
#2번째 컴파일러 : 공백(목사)로공백재직
#3번째 컴파일러 : 공백(부동산중개업)을공백한다
#4번째 컴파일러 : 공백(국제결혼중개업자)가공백

cv_compiler['cv_relation_exact_stamp'] = [re.compile('자신의\s(%s)인'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)인\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)관계이다'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)관계에\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)를\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)을\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)과\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)의\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)와\s'%('|'.join(relations.relation_dict))),
                                          re.compile('\s(%s)에게\s'%('|'.join(relations.relation_dict)))]

#1번째 컴파일러 : 자신의공백(어머니)인
#2번째 컴파일러 : 공백(동거인)인공백
#3번째 컴파일러 : 공백(연인)관계이다.
#4번째 컴파일러 : 공백(내연)관계에공백
#5번째 컴파일러 : 공백(친구)를공백
#6번째 컴파일러 : 공백(형)을공백
#7번째 컴파일러 : 공백(남편)과공백
#8번째 컴파일러 : 공백(부모)의공백
#9번째 컴파일러 : 공백(친구)와공백
#10번째 컴파일러 : 공백(친정어머니)에게공백

cv_compiler['cv_law_total_stamp'] = [re.compile('\s([가-힣]{1,10}법\s제\d{,3}조의?\s?제?\d{,2}항?\s?제?\d{,2}호?)'),
                                     re.compile('([가-힣]{1,20}법률)\s(제\d{,3}조의?\s?제?\d{,2}항?\s?제?\d{,2}호?)'),
                                     re.compile('(%s)(의\s점)'%('|'.join(laws.law_dict['all_crime']))),
                                     re.compile('(수차례)(%s)을'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('(수차례)(%s)를'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('(%s)(를\s하는)'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('(피해자를\s)(%s)'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('\s(%s)(하기에)'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('\s(%s범죄)(를)\s'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('(\d{1}\.)\s(%s)\s'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('\s(%s)(하려)'%('|'.join(laws.law_dict['main_crime']))),
                                     re.compile('\s(%s)(만을)'%('|'.join(laws.law_dict['main_crime'])))]
#1번째 컴파일러 : [공백(형법공백제298조)]
#2번째 컴파일러 : (특정범죄가중처벌등에관한법률)공백(제5조의4) -> () () 공백 합침
#3번째 컴파일러 : (절도)(의공백점) -> ()() 공백없이 합침
#4번째 컴파일러 : (수차례)(폭행)을 -> ()() 공백없이 합침
#5번째 컴파일러 : (수차례)(폭행)를 -> ()() 공백없이 합침
#6번째 컴파일러 : (성매수)(를공백하는) -> ()() 공백없이 합침
#7번째 컴파일러 : (피해자를공백)(납치) -> ()() 공백없이 합침
#8번째 컴파일러 :  공백(살해)(하기에) -> ()() 공백없이 합침
#9번째 컴파일러 : 공백(살인범죄)(를)공백  -> ()() 공백없이 합침
#10번째 컴파일러 : (2.)공백(현주건조물방화)공백 -> () () 공백 합침
#11번째 컴파일러 : 공백(살해)(하려) -> ()() 공백없이 합침
#12번째 컴파일러 : 공백(상해)(만을) -> ()() 공백없이 합침
cv_compiler['cv_law_small_stamp'] = [(re.compile('([가-힣]{1,10}법)\s(제\d{,3}조의?\s?제?\d{,2}항?\s?제?\d{,2}호?)'),
                                      ['cv_law', 'qt_law']),
                                     (re.compile('([가-힣]{1,20}법률)\s(제\d{,3}조의?\s?제?\d{,2}항?\s?제?\d{,2}호?)'),
                                      ['cv_law','qt_law']),
                                     (re.compile('(%s)의\s점'%('|'.join(laws.law_dict['all_crime']))),
                                      ['cv_law']),
                                     (re.compile('수차례(%s)을'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('수차례(%s)를'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('(%s)를\s하는'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('(피해자)를\s(%s)'%('|'.join(laws.law_dict['main_crime']))),
                                      ['ps_court', 'cv_law']),
                                     (re.compile('(%s)하기에'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('(%s범죄)를'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('\d{1}\.\s(%s)'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('(%s)하려'%('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law']),
                                     (re.compile('(%s)만을' % ('|'.join(laws.law_dict['main_crime']))),
                                      ['cv_law'])]

