def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    middle = [pivot] + [x for x in arr[1:] if x == pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [41,11,83,47,92,29,74,20]
sorted_arr = quick_sort(arr)
print(sorted_arr)  



