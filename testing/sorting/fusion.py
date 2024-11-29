def fusion(TA, TB):
    T = []
    while TA != [] and TB != []:
        if TA[0] < TB[0]:
            T.append(TA.pop(0))
        else:
            T.append(TB.pop(0))
    return T + TA + TB

def tri_fusion(T):
    if len(T) <= 1:
        return T
    else:
        m = len(T) // 2
        TA = tri_fusion(T[:m])
        TB = tri_fusion(T[m:])
        return fusion(TA, TB)
    
print(tri_fusion([3, 4, 6, 2, 5, 1, 8, 7]))