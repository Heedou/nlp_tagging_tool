import re

def split_sub_concat(temp_text, found, tag, or_list, reor_list):
    import re
    #temp_text = '피의자는 2019.1.1경 피의자였다.'
    #found = ['2019.1.1','피의자']
    #tag = ['DT', 'PS']
    #print((temp_text, found))
    origin_text = temp_text

    substitution_list = []
    for i in found:
        target = i
        index = -1
        while True:
            index = temp_text.find(target, index + 1)
            if index == -1:
                break
            substitution_list.append((index, target))
    for i in found:
        temp_text = re.sub(i, '쀍씛', temp_text)

        #print(temp_text)
    #temp_text = '쀍씛는 쀍씛경 쀌씛였다.'
    #substitution_list = [(0, '피의자'), (15, '피의자'), (5, '2019.1.1')]
    #print(substitution_list)

    substitution_list.sort(key = lambda x : x[0])
    #substitution_list = [(0, '피의자'), (5, '2019.1.1'), (15, '피의자')]


    after = temp_text.split('쀍씛')
    for i in range(len([i for i in after if i==''])):
        if '' in after:
            after.remove('')
    #after : ['는 ','경 ','였다.']

    after_list = []
    PPPack_list = []
    after_overlap_eliminated = list(set(after))
    for i in after:
        target = i
        index = temp_text.find(target)
        after_list.append((index, target))
    index=-1
    while True:
        index = temp_text.find('쀍씛', index + 1)
        if index == -1:
            break
        PPPack_list.append((index, '쀍씛'))
    #PPPack_list = [(0, '쀍씛'),(4, '쀍씛'),(8, '쀍씛')]
    #after_list = [(2, '는 '), (6, '경 '), (10, '였다.')]


    after_sub = []
    try:
        for f, t in zip(found, tag):
            after_sub.append(re.sub(f, '<%s : %s>' % (f,t), f))
    except:
        for f in found:
            after_sub.append(re.sub(f, '<%s : %s>' % (f,tag), f))
    #after_sub : ['<2019.1.1 : DT>','<피의자 : PS>']

    after_sub = back_to_orginalorder(or_list, reor_list, after_sub)
    # after_sub : ['<피의자 : PS>','<2019.1.1 : DT>']
    #print(after_sub)

    matched_result = []
    for i in range(len(substitution_list)):
        try:
            position = PPPack_list[i][0]  # 0
            text_ = substitution_list[i][1]  # 피의자
            for i in range(len(after_sub)):
                match = after_sub[i]
                match = match.split(' : ')[0]  # <피의자
                match = re.sub('<', '', match)  # 피의자
                if match == text_:
                    text_ = after_sub[i]  # <피의자 : PS>
            matched_result.append((position, text_))
        except:
            pass
    # matched_result = [(0, '<피의자 : PS>'), (4, '<2019.1.1 : DT>'), (8, '<피의자 : PS>')]
    #print(matched_result)
    final_result = after_list + matched_result
    final_result.sort(key=lambda x: x[0])
    # final_result = [(0, '<피의자 : PS>'), (2, '는 '),(4, '<2019.1.1 : DT>'),(6, '경 '), (8, '<피의자 : PS>'),(10, '였다.')]

    all = ''
    for final in final_result:
        all += final[1]

    return all


def back_to_orginalorder(or_list, reor_list, txt_corrected_list):
    # or_list : 본래 리스트, ex)['사과', '바나나', '포도', '망고', '수박']
    # reor_list : 본래 리스트에서 어떤 기준에 의해 순서가 바뀐 리스트, ex) ['바나나', '망고', '포도', '수박', '사과']
    # txt_corrected_list : reor_list의 요소별 순서를 유지하며 변형을 가한 리스트, ex)['바나나<과일>', '망고<과일>', '포도<과일>', '수박<과일>', '사과<과일>']

    # 본래 리스트의 요소별 순서를 기억해놨다가 그 순서만 되돌리는 코드
    order = [i for i in range(len(or_list))]
    after_order = [reor_list.index(or_list[i]) for i in range(len(or_list))]
    return [txt_corrected_list[after_order[i]] for i in range(len(or_list))]

def make_small_tag(total_tag_list, tag, text):
    # total_tag_list = ['ps_court&name_total', PS_compiler.ps_compiler['ps_court&name_small_stamp']]
    total_tag = total_tag_list[0]  #'ps_court&name_total'
    compilers = total_tag_list[1]  #PS_compiler.ps_compiler['ps_court&name_small_stamp']
    if total_tag in tag:
        compilers.sort(key = lambda x: len(str(x[0])), reverse=True)
        for i in range(len(compilers)):
            compiler = compilers[i][0]
            temp_tag = re.sub('<', '', tag)
            temp_tag2 = re.sub('<', '', tag)
            #num_of_found_tag = 0
            if len(compiler.findall(temp_tag)) > 0:
                found_en = []
                for com in compiler.findall(temp_tag):
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

                for f, t in zip(found_en,
                                compilers[i][1]):
                    temp_tag2 = re.sub(f, '<%s : %s>' % (f, t), temp_tag2)
                    #print(temp_tag2)
                try:
                    temp_tag2 = re.sub(' : %s>'%total_tag, '', temp_tag2)
                    temp_tag2 = re.sub(': %s>'%total_tag, '', temp_tag2)
                    #print(temp_tag2)
                except:
                    pass
                try:
                    text = re.sub(temp_tag, temp_tag2, text)
                    text = re.sub('<<', '<', text)
                    #print(temp_text)
                except :
                    pass


    return text