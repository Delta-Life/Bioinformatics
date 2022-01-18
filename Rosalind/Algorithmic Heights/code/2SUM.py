# 2SUM
# http://rosalind.info/problems/2sum/

from utilities import get_file, get_answer_file

def two_sum(num_array):
    minus_set = set(-i for i in num_array)
    for i, value in enumerate(num_array):
        if value in minus_set:
            try:
                j = num_array.index(-value, i+1)
            except ValueError:
                continue

            return (i+1, j+1)   
    return (-1, -1)


with get_file() as file:
    k, n = map(int, file.readline().split())
    num_arrays = [list(map(int, line.split())) for line in file.readlines()]

with get_answer_file() as file:
    for num_array in num_arrays:
        p, q = two_sum(num_array)
        if p == -1:
            print(-1, file=file)
        else:
            print(p, q, file=file)