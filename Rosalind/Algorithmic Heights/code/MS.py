# Merge Sort
# http://rosalind.info/problems/ms/

from utilities import get_file, get_answer_file

def merge_sort(num_array):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if num_array[l] < num_array[h]:
                temp.append(num_array[l])
                l += 1
            else:
                temp.append(num_array[h])
                h += 1
        
        while l < mid:
            temp.append(num_array[l])
            l += 1
        while h < high:
            temp.append(num_array[h])
            h += 1
        
        for i in range(low, high):
            num_array[i] = temp[i - low]

    return sort(0, len(num_array))


with get_file() as file:
    size_of_array = int(file.readline().rstrip())
    num_array = list(map(int, file.readline().split()))

with get_answer_file() as file:
    merge_sort(num_array)
    print(" ".join(map(str, num_array)), file=file)