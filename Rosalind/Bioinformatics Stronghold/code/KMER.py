# k-Mer Composition
# http://rosalind.info/problems/kmer/

from itertools import product
from utilities import get_file, read_FASTA, get_answer_file

def kmer_composition(strand, k):
    kmer_array = [''.join(x) for x in product('ATGC', repeat=k)]
    kmer_array.sort()
    result = [0] * len(kmer_array)
    for n, i in enumerate(kmer_array):
        for j in range(len(strand)-3):
            if strand[j:j+4] == i:
                result[n] += 1
    return result
        

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print(" ".join(map(str, kmer_composition(strand_array[0], 4))), file=file)