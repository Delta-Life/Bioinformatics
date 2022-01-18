# Generate the Frequency Array of a String
# https://rosalind.info/problems/ba1k/

from itertools import product
from utilities import get_file, get_answer_file

def most_frequent_kmer(k, strand):
    kmer_dict = {"".join(i):0 for i in product("ATGC", repeat=k)}
    for i in range(len(strand)-k+1):
        kmer_dict[strand[i:i+k]] += 1
    return [kmer_dict[k] for k in sorted(kmer_dict.keys())]

with get_file() as file:
    strand = file.readline().rstrip()
    k = int(file.readline().rstrip())

with get_answer_file() as file:
    print(" ".join(map(str, most_frequent_kmer(k, strand))), file=file)