# Partial Permutations
# http://rosalind.info/problems/pper/

from utilities import get_file, get_answer_file
from functools import reduce

def get_part_perm(n, k):
    return reduce(lambda x, y: x*y%1000000, range(n-k+1, n+1), 1)

with get_file() as file:
    n, k = map(int, file.readline().split())

with get_answer_file() as file:
    part_perm = get_part_perm(n, k)
    print(part_perm, file=file)