# Building a Heap
# http://rosalind.info/problems/hea/

from utilities import get_file, get_answer_file

def get_max_heap(num_array):
    for index, num in enumerate(num_array):
        while num_array[index//2] < num:
            num_array[index//2], num_array[index] = num_array[index], num_array[index//2]
            index = index//2
    
    return num_array


with get_file() as file:
    size_of_heap = int(file.readline().rstrip())
    num_array = [100000] + list(map(int, file.readline().split()))

with get_answer_file() as file:
    print(" ".join(map(str, get_max_heap(num_array)[1:])), file=file)