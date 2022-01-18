# Error Correction in Reads
# http://rosalind.info/problems/corr/

from collections import Counter
from utilities import get_file, read_FASTA, get_complement_strand, get_answer_file

def hamming(seq1, seq2):
    return sum(seq1[i] != seq2[i] for i in range(len(seq1)))

def error_correction(strand_array):
    complement_strand_array = [get_complement_strand(strand_array[i]) for i in range(len(strand_array))]
    counts = Counter(strand_array + complement_strand_array)
    corrects = [i for i in counts  if counts[i]>1]
    result = []
    for i in strand_array:
        if counts[i]<2:
            for j in corrects:
                if hamming(i, j) == 1:
                    result.append(i)
                    result.append(j)
    return result

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    corrections = error_correction(strand_array)
    for i in range(0, len(corrections), 2):
        print(corrections[i]+"->"+corrections[i+1], file=file)