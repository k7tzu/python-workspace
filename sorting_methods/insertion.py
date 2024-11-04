def insertion_sort(arr):
    if len(arr) <= 1:
        return arr, "Already sorted"
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#arr = [1]   
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))