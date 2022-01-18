# Implement MotifEnumeration
# https://rosalind.info/problems/ba2a/

from itertools import product
from utilities import get_file, get_answer_file, hamming_distance

def most_frequent_kmer(k, strand_array, d):
    result = {"".join(i):[0]*len(strand_array) for i in product("ATGC", repeat=k)}
    for n, strand in enumerate(strand_array):
        for i in range(len(strand)-k+1):
            for j in result.keys():
                if hamming_distance(strand[i:i+k], j) <= d:
                    result[j][n] = 1
    return sorted([key for key, value in result.items() if sum(value)==len(strand_array)])

with get_file() as file:
    k, d = map(int, file.readline().split())
    strand_array = []
    for i in file.readlines():
        strand_array.append(i.rstrip())

with get_answer_file() as file:
    print(" ".join(most_frequent_kmer(k, strand_array, d)), file=file)