
def delete_subset(list1, list2):
    """
    list1=['2010년 1월 1일']에서 list2=['2010년 1']중
    하나가 부분집합으로 발견된 부분은 리스트에서 제외하는 함수
    """
    try:
        for_remove = []
        for found2 in list2:
            check = 0
            for found1 in list1:
                if found2 in found1:
                    check += 1
            if check != 0:
                for_remove.append(found2)
    except:
        pass
    try:
        for remove in for_remove:
            list2.remove(remove)
    except:
        pass

def make_one_list(lists):
    """
    여러개의 리스트를 하나의 리스트로 합쳐주는 함수
    """
    result = []
    for list_ in lists:
        result.extend(list_)
    return result

def delete_subset_in_onelist(list_):
    """
    한 리스트 안에서 한 요소가 다른 요소의 부분집합이 된다면 그 요소를 삭제해주는 함수
    """
    to_remove=[]
    for found in list_:
      check=0
      for pound in list_:
        if found != pound and found in pound:
          check += 1
      if check>0:
        to_remove.append(found)
    to_remove=list(set(to_remove))
    for remove in to_remove:
      list_.remove(remove)


def delete_subset_in_onelist2(list_):
    """
    [('2011. 1. 3.', 'DT'), ('1. 3.', 'DT')] 에서 부분집합인 '1. 3.' 지워주는 함수
    """
    to_remove = []

    for i in range(len(list_)):
        found = list_[i][0]
        check = 0
        for k in range(len(list_)):
            pound = list_[k][0]
            if found != pound and found in pound:
                check += 1
        if check > 0:
            to_remove.append((found, list_[i][1]))
    to_remove = list(set(to_remove))

    for remove in to_remove:
        list_.remove(remove)

    return list_

def back_to_orginalorder_intxt(std_txt, list_to_correct):
    """
    기준 텍스트에서 여러가지 패턴을 추출했는데, 텍스트내에서의 순서와 다를 경우,
    텍스트 내에서의 순서대로 패턴들을 정렬해주는 함수
    """
    original_order = [int(i) for i in range(len(list_to_correct))]
    original_index = [int(std_txt.find(list_to_correct[i])) for i in range(len(list_to_correct))]
    after_index = [i for i in original_index]
    after_index.sort(reverse=False)
    list_to_correct = [list_to_correct[original_order.index(original_index.index(after_index[i]))] for i in range(len(after_index))]
    return list_to_correct

def concat_tuple_in_list(list_, indexes, num_of_compo, concat_sign):
    """
    어떤 list_[index] 안에 ('', '')튜플 형식으로 데이터가 들어 있을 때
    concat_sign기준으로 하나의 텍스트 ''로 고쳐주는 함수
    """
    if num_of_compo == 2:
        for index in indexes:
            try:
                changed = []
                for i in range(len(list_[index])):
                    if len(list_[index][i])==2:
                        changed.append(list_[index][i][0] + concat_sign + list_[index][i][1])
                    else:
                        changed.append(list_[index][i])
                list_[index] = changed
            except:
                pass
    elif num_of_compo == 3:
        for index in indexes:
            try:
                changed = []
                for i in range(len(list_[index])):
                    if len(list_[index][i])==3:
                        changed.append(list_[index][i][0] + concat_sign[0] + list_[index][i][1]\
                                       +concat_sign[1] + list_[index][i][2])
                    else:
                        changed.append(list_[index][i])
                list_[index] = changed
            except:
                pass
    elif num_of_compo == 4:
        for index in indexes:
            try:
                changed = []
                for i in range(len(list_[index])):
                    if len(list_[index][i])==4:
                        changed.append(list_[index][i][0] + concat_sign[0] + list_[index][i][1]\
                                       +concat_sign[1] + list_[index][i][2] + concat_sign[2]\
                                       +list_[index][i][3])
                    else:
                        changed.append(list_[index][i])
                list_[index] = changed
            except:
                pass
    elif num_of_compo == 5:
        for index in indexes:
            try:
                changed = []
                for i in range(len(list_[index])):
                    if len(list_[index][i])==5:
                        changed.append(list_[index][i][0] + concat_sign[0] + list_[index][i][1]\
                                       +concat_sign[1] + list_[index][i][2] + concat_sign[2]\
                                       +list_[index][i][3] + concat_sign[3] + list_[index][i][4])
                    else:
                        changed.append(list_[index][i])
                list_[index] = changed
            except:
                pass

def select_tuple_in_list(list_, indexes, num_of_compo, select_index):
    """
    어떤 list_[index] 안에 ('', '')튜플 형식으로 데이터가 들어 있을 때
    원하는 인덱스만 가지고 오는 함수
    """
    for index in indexes:
        try:
            changed = []
            for i in range(len(list_[index])):
                if len(list_[index][i]) == num_of_compo:
                    changed.append(list_[index][i][select_index])
                else:
                    changed.append(list_[index][i])
            list_[index] = changed
        except:
            pass