# Reconstruct a String from its k-mer Composition
# https://rosalind.info/problems/ba3h/

from utilities import get_file, get_answer_file

def get_superstring(strand_array):
    strand = strand_array.pop(0)
    k = len(strand) - 1
    while len(strand_array) != 0:
        for i in strand_array:
            if strand[-k:] == i[:k]:
                strand = strand + i[-1]
                strand_array.remove(i)
            elif strand[:k] == i[-k:]:
                strand = i[0] + strand
                strand_array.remove(i)
    return strand

with get_file() as file:
    k = int(file.readline().rstrip())
    strand_array = [i.rstrip() for i in file.readlines()]

with get_answer_file() as file:
    print(get_superstring(strand_array), file=file)