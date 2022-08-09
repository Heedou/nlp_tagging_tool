import re
import sys, os
base = os.path.abspath(__file__).replace(r'\re_compiler\LC_compiler.py','')
sys.path.append(os.path.dirname(base+r'\dictionary'))

from dictionary import locations

import re
lc_compiler = {}
lc_compiler['lc_total_stamp'] = [re.compile('([가-힣]{2,5}시)\s([가-힣]{1,3}구)\s([가-힣\s\d\-]{1,10}길)\s([\d\-]{1,6})'),
                                 re.compile('([가-힣]{2,5}시)\s([가-힣]{1,3}구)\s([가-힣\s\d\-]{1,10}길)\s([\d\-]{1,6})([가-힣]{1,4}동)'),
                                 re.compile('([가-힣]{1,4}도)\s([가-힣]{2,5}시)\s([가-힣]{1,3}읍)\s([가-힣\s\d]{1,5}로)\s([\d\-]{1,6})'),
                                 re.compile('([가-힣]{2,5}시)\s([가-힣]{1,3}구)\s([가-힣]{1,4}동)\s([가-힣\s\d]{1,5}로)\s([\d\-]{1,6})'),
                                 re.compile('(%s)\s([가-힣]{1,3}구)\s([a-zA-Z]{1,3})'%('|'.join(locations.location_dict['main_city']))),
                                 re.compile('(%s)\s([[가-힣]{2,5}시])\s([가-힣\d\-]{1,10}길)\s([\d\-]{1,6})'\
                                            %('|'.join(locations.location_dict['main_province']))),
                                 re.compile('(%s)\s([가-힣○]{,3}구)\s([가-힣○]{,3}동)'\
                                            %('|'.join(locations.location_dict['main_city']))),
                                 re.compile('(%s)\s([가-힣]{1,8}역)'% ('|'.join(locations.location_dict['main_city']))),
                                 re.compile('(%s)\s([가-힣○]{1,3}군)\s([가-힣○]{1,3}면)'\
                                            %('|'.join(locations.location_dict['main_province']))),
                                 re.compile('(%s)\s([가-힣○]{,3}구)' % ('|'.join(locations.location_dict['main_city']))),
                                 re.compile('([가-힣]{1,3}시)\s에\s있는'),
                                 re.compile('([가-힣]{1,3}시)\s소재'),
                                 re.compile('([가-힣]{1,3}도)\s([가-힣]{1,3}군)\s([가-힣]{1,3}면)\s([가-힣\s\d\-]{1,10}길)\s([\d\-]{1,6})'),
                                 re.compile('\s([가-힣]{1,3}시)\s([가-힣○]{,3}구)\s([가-힣○]{,3}동)\s앞\s'),
                                 re.compile('\s([가-힣]{1,3}시)\s([가-힣○]{,3}구)\s([가-힣○]{,3}읍)'),
                                 re.compile('\s(%s)\s([가-힣○]{,3}읍)\s([가-힣○]{,3}리)'%('|'.join(locations.location_dict['main_province']))),
                                 re.compile('\s(%s)\s'% ('|'.join(locations.location_dict['main_city'])))]
#1번째 컴파일러 : ([부산광역]시)공백([연제]구)공백([거제천로152]번길)공백([19]) -> 그룹 (city) (county) (road) (건물번호)
#2번째 컴파일러 : ([대전광역]시)공백([중]구)공백([당디로56]번길)공백([16])공백([산성]동) -> 그룹 (city) (county) (road) (건물번호) (county)
#3번째 컴파일러 : ([경기]도)공백([김포]시)공백([통진]읍)공백([옹정로])공백([220]) -> (province) (city) (county) (road) (건물번호)
#4번째 컴파일러 : ([인천광역]시)공백([부평]구)공백([부평]동)공백([길주남로])공백([48]) -> (city) (county) (county) (road) (건물번호)
#5번째 컴파일러 : (부산or서울or대전 등)공백([금정]구)공백([G]) -> (city) (county) (others)
#6번째 컴파일러 : (경남or경북or경기 등)공백([사천]시)공백([임내]길)공백([79]) -> (province) (city) (road) (건물번호)
#7번째 컴파일러 : (울산or대구 등)공백(구)공백(동) -> (city) (county) (county)
#8번째 컴파일러 : (서울or대전 등)공백([]역) -> (city) (others)
#9번째 컴파일러 : (전남 등)공백([함평]군)공백([]면) -> (province) (county) (county)
#10번째 컴파일러 : (인천 등)공백(구) -> (city) (county)
#11번째 컴파일러 : ([파주]시)공백에공백있는 -> (city)
#12번째 컴파일러 : ([구미]시)공백소재 -> (city)
#13번째 컴파일러 : ([경상북]도)공백([봉화]군)공백([소천]면)공백([숲터]길)공백([12]) -> (province) (county) (county) (road) (건물번호)
#14번째 컴파일러 : 공백(서울시)공백(송파구)공백(가락동)공백앞공백 -> (city) (county) (county)
#15번째 컴파일러 : 공백(용인시)공백(00구)공백(00읍) -> (city) (county) (countY)
#16번째 컴파일러 : 공백(강원)공백(홍천읍)공백(○○○리) -> (province) (countY) (countY)
#17번째 컴파일러 : 공백(파주시)공백 -> (city)

lc_compiler['lc_small_stamp'] = [(re.compile('([가-힣]{2,5}시)\s([가-힣]{1,3}구)\s([가-힣\s\d\-]{1,10}길)\s([\d\-]{1,6})'),
                                  ['lc_city','lc_county','af_road','building_num']),
                                 (re.compile('([가-힣]{2,5}시)\s([가-힣]{1,3}구)\s([가-힣\s\d\-]{1,10}길)\s([\d\-]{1,6})([가-힣]{1,4}동)'),
                                  ['lc_city','lc_county','af_road','building_num', 'lc_county']),
                                 (re.compile('([가-힣]{1,4}도)\s([가-힣]{2,5}시)\s([가-힣]{1,3}읍)\s([가-힣\s\d]{1,5}로)\s([\d\-]{1,6})'),
                                  ['lc_province','lc_city','lc_county','af_road','building_num']),
                                 (re.compile('([가-힣]{2,5}시)\s([가-힣]{1,3}구)\s([가-힣]{1,4}동)\s([가-힣\s\d]{1,5}로)\s([\d\-]{1,6})'),
                                  ['lc_city','lc_county','lc_county','af_road','building_num']),
                                 (re.compile('(%s)\s([가-힣]{1,3}구)\s([a-zA-Z]{1,3})'%('|'.join(locations.location_dict['main_city']))),
                                  ['lc_city','lc_county','lc_others']),
                                 (re.compile('(%s)\s([[가-힣]{2,5}시])\s([가-힣\d\-]{1,10}길)\s([\d\-]{1,6})'\
                                            %('|'.join(locations.location_dict['main_province']))),
                                  ['lc_province','lc_city','af_road','buidling_num']),
                                 (re.compile('(%s)\s([가-힣○]{,3}구)\s([가-힣○]{,3}동)'\
                                            %('|'.join(locations.location_dict['main_city']))),
                                  ['lc_city','lc_county','lc_county']),
                                 (re.compile('(%s)\s([가-힣]{1,8}역)'% ('|'.join(locations.location_dict['main_city']))),
                                  ['lc_city','lc_others']),
                                 (re.compile('(%s)\s([가-힣○]{1,3}군)\s([가-힣○]{1,3}면)'\
                                            %('|'.join(locations.location_dict['main_province']))),
                                  ['lc_province','lc_county', 'lc_county']),
                                 (re.compile('(%s)\s([가-힣○]{,3}구)' % ('|'.join(locations.location_dict['main_city']))),
                                  ['lc_city','lc_county']),
                                 (re.compile('([가-힣]{1,3}시)\s에\s있는'),
                                  ['lc_city']),
                                 (re.compile('([가-힣]{1,3}시)\s소재'),
                                  ['lc_city']),
                                 (re.compile('([가-힣]{1,3}도)\s([가-힣]{1,3}군)\s([가-힣]{1,3}면)\s([가-힣\s\d\-]{1,10}길)\s([\d\-]{1,6})'),
                                  ['lc_province','lc_county','lc_county','af_road','building_num']),
                                 (re.compile('([가-힣]{1,3}시)\s([가-힣○]{,3}구)\s([가-힣○]{,3}동)\s앞\s'),
                                  ['lc_city','lc_county','lc_county']),
                                 (re.compile('([가-힣]{1,3}시)\s([가-힣○]{,3}구)\s([가-힣○]{,3}읍)'),
                                  ['lc_city', 'lc_county', 'lc_county']),
                                 (re.compile('(%s)\s([가-힣○]{,3}읍)\s([가-힣○]{,3}리)'\
                                            %('|'.join(locations.location_dict['main_province']))),
                                  ['lc_province', 'lc_county', 'lc_county']),
                                 (re.compile('(%s)'% ('|'.join(locations.location_dict['main_city']))),
                                  ['lc_city'])]


