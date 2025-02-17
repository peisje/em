def filtreeri_arvud(andmed):
    nums = []
    for num in andmed:
        if num % 10 == 0:
            nums.append(num)
    return tuple(nums)

def leia_indeks(tupleInfo,findElem):
     for elem in tupleInfo:
        if findElem in tupleInfo:
            tulemus = tupleInfo.index(findElem)
        else:
            tulemus = -1
            return tulemus
