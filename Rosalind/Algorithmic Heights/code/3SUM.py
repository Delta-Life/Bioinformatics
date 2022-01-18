# 3SUM
# http://rosalind.info/problems/3sum/

from utilities import get_file, get_answer_file

def get_3sum(array):
    index_dict = {i:n for n, i in enumerate(array)}
    array.sort()
    for left in range(len(array)-2):
        mid = left + 1
        right = len(array) - 1
        while mid < right:
            if array[left] + array[mid] + array[right] == 0:
                return [index_dict[array[left]]+1, index_dict[array[mid]]+1, index_dict[array[right]]+1]
            elif array[left] + array[mid] + array[right] > 0:
                right -= 1
            else:
                mid += 1
    return [-1]

with get_file() as file:
    len_input, len_array = map(int, file.readline().split())
    input_array = []
    for i in file.readlines():
        input_array.append(list(map(int, i.split())))

with get_answer_file() as file:
    for i in input_array:
        print(" ".join(map(str, sorted(get_3sum(i)))), file=file)