# Mendel's First Law
# http://rosalind.info/problems/iprb/

from utilities import get_file, comb, get_answer_file

def dominant_allele(k, m, n):
    t = k + m + n
    return (1 - comb(m, 2)/comb(t, 2)/4 - m*n/comb(t, 2)/2 - comb(n, 2)/comb(t, 2))

with get_file() as file:
    k, m, n = map(int, file.readline().split())

with get_answer_file() as file:
    print(dominant_allele(k, m, n))