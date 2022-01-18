# Counting Subsets
# https://rosalind.info/problems/sset/

from utilities import get_file, get_answer_file

def get_num_of_subsets(n):
    result = 1
    for i in range(n):
        result = result * 2 % 1000000
    return result

with get_file() as file:
    n = int(file.readline().rstrip())

with get_answer_file() as file:
    print(get_num_of_subsets(n), file=file)