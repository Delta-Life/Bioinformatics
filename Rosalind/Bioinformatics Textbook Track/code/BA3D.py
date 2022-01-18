# Construct the De Bruijn Graph of a String
# https://rosalind.info/problems/ba3d/

from utilities import get_file, get_answer_file
from collections import defaultdict

def de_bruijn(k, strand):
    kmer_dict = defaultdict(list)
    
    for i in range(len(strand)-k):
        kmer_dict[strand[i:i+k]].append(strand[i+1:i+k+1])
    
    return kmer_dict

with get_file() as file:
    k = int(file.readline().rstrip()) - 1
    strand = file.readline().rstrip()

with get_answer_file() as file:
    for i, j in de_bruijn(k, strand).items():
        print(i, "->", ",".join(j), file=file)