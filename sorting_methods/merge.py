def merge(TA, TB):
    T = []
    while TA != [] and TB != []:
        if TA[0] < TB[0]:
            T.append(TA.pop(0))
            # -- ALTERNATIVE
            #T.append(TA[0])
            #TA.pop(0)
        else:
            T.append(TB.pop(0))
            # -- ALTERNATIVE
            #T.append(TB[0])
            #TB.pop(0)
    return T + TA + TB

def merge_sort(T):
    if len(T) <= 1:
        return T
    else:
        m = len(T) // 2
        TA = merge_sort(T[:m])
        TB = merge_sort(T[m:])
        return merge(TA, TB)
    
print(merge_sort([3, 4, 6, 2, 5, 1, 8, 7]))