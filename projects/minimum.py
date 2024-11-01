def minimum(arr):
    if not arr:
        return "target is empty"
    else:
        min_value = arr[0]
        min_index = 0
        for i in range(1, len(arr)):
            if min_value > arr[i]:
                min_value = arr[i]
                min_index = i
    return min_value, min_index

arr = [70, 4, 49, -2, 1, 23]
print(minimum(arr))