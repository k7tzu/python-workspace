def enumere(tab):
    result = {}
    for i in range(len(tab)):
        value = tab[i]
        if value not in result:
            result[value] = []
        result[value].append(i)
    return result

print(enumere([]))
print(enumere([1, 2, 3]))
print(enumere([1, 1, 2, 3, 2, 1]))