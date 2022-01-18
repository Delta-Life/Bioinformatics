# Construct the De Bruijn Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3e/

from utilities import get_file, get_answer_file
from collections import defaultdict

def de_bruijn(strand_array):
    kmer_dict = defaultdict(list)
    k = len(strand_array[0])-1
    
    for i in strand_array:
        kmer_dict[i[:k]].append(i[-k:])

    return kmer_dict

with get_file() as file:
    strand_array = [i.rstrip() for i in file.readlines()]

with get_answer_file() as file:
    for i, j in de_bruijn(strand_array).items():
        print(i, "->", ",".join(j), file=file)