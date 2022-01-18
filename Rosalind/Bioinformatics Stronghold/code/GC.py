# Computing GC Content
# http://rosalind.info/problems/gc/

from utilities import get_file, read_FASTA, argmax, get_answer_file
from collections import Counter

def GCcontent(nameArr, strandArr):
    GC_array = []

    for strand in strandArr:
        counts = Counter(strand)
        GC_array.append((counts['G']+counts['C']) * 100 / len(strand))
    
    return GC_array

with get_file() as file:
    name_array, strand_array = read_FASTA(file)
    GC_array = GCcontent(name_array, strand_array)

with get_answer_file() as file:
    print(name_array[argmax(GC_array)], file=file)
    print(GC_array[argmax(GC_array)], file=file)