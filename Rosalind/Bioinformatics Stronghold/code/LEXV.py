# Ordering Strings of Varying Length Lexicographically
# https://rosalind.info/problems/lexv/

from itertools import product
from utilities import get_file, get_answer_file

def alpha_comb(alphabet, n):
    result = []
    def comb(n, acc=''):
        if n > 0:
            for c in alphabet:
                result.append(acc + c)
                comb(n - 1, acc + c)
    comb(n, '')
    return result

with get_file() as file:
    string = list(file.readline().split())
    num = int(file.readline().rstrip())

with get_answer_file() as file:
    for i in alpha_comb(string, num):
        print("".join(i), file=file)