# Merge Two Sorted Arrays
# http://rosalind.info/problems/mer/

from utilities import get_file, get_answer_file

def merge(arr1, arr2):
    sortedArray = []
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            sortedArray.append(arr1.pop(0))
        else:
            sortedArray.append(arr2.pop(0))

    if len(arr1) == 0:
        sortedArray += arr2
    else:
        sortedArray += arr1
    
    return sortedArray


with get_file() as file:
    len1 = int(file.readline().rstrip())
    arr1 = list(map(int, file.readline().split()))
    len2 = int(file.readline().rstrip())
    arr2 = list(map(int, file.readline().split()))

with get_answer_file() as file:
    sorted_array = merge(arr1, arr2)
    print(" ".join(map(str, sorted_array)), file=file)