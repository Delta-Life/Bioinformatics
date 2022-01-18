# 2-Way Partition
# http://rosalind.info/problems/par/

from utilities import get_file, get_answer_file

def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left_arr, equal_arr, right_arr = [], [], []
    for num in arr:
        if num < pivot:
            left_arr.append(num)
        elif num > pivot:
            right_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort2(left_arr) + equal_arr + quick_sort2(right_arr)

def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return
        
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)
    
    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    
    return sort(0, len(arr) - 1)

with get_file() as file:
    len_array = int(file.readline().rstrip())
    num_array = list(map(int, file.readline().split()))

with get_answer_file() as file:
    quick_sort(num_array)
    print(" ".join(map(str, num_array)), file=file)