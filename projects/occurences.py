def occurences(arr):
    counter = {}
    for item in arr:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter

arr = [1, 2, 2, 3, 3, 3, 4]
print(occurences(arr))