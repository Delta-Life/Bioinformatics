# Find the Most Frequent Words with Mismatches in a String
# https://rosalind.info/problems/ba1i/

from itertools import product
from utilities import get_file, get_answer_file, hamming_distance

def most_frequent_kmer(k, strand, d):
    kmer_dict = {"".join(i):0 for i in product("ATGC", repeat=k)}
    for i in range(len(strand)-k+1):
        for j in kmer_dict.keys():
            if hamming_distance(strand[i:i+k], j) <= d:
                kmer_dict[j] += 1
    return [k for k,v in kmer_dict.items() if max(kmer_dict.values())==v]

with get_file() as file:
    strand = file.readline().rstrip()
    k, d = map(int, file.readline().split())

with get_answer_file() as file:
    print(" ".join(most_frequent_kmer(k, strand, d)), file=file)