# Introduction to Alternative Splicing
# https://rosalind.info/problems/aspc/

import math
from utilities import get_file, get_answer_file

def get_num_of_total_subsets(n, m):
    result = 0
    for i in range(m, n+1):
        result = (result + math.comb(n, i)) % 1000000
    return result

with get_file() as file:
    n, m = map(int, file.readline().split())

with get_answer_file() as file:
    print(get_num_of_total_subsets(n, m), file=file)