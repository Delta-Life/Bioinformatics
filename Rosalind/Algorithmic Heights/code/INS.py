# Insertion Sort
# http://rosalind.info/problems/ins/

from utilities import get_file, get_answer_file

def INS_count(array):
    count = 0

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                count += 1
            else:
                break
    
    return count

with get_file() as file:
    len_of_array = int(file.readline().rstrip())
    array = list(map(int, file.readline().split()))

with get_answer_file() as file:
    count = INS_count(array)
    print(count, file=file)