# Speeding Up Motif Finding
# http://rosalind.info/problems/kmp/

from utilities import get_file, read_FASTA, get_answer_file

def failure_array(strand):
    result = [0] * len(strand)
    longest_motif = 0
    for i in range(len(strand)):
        for j in range(1, len(strand)-i+1):
            if strand[:i] == strand[j:j+i]:
                result[j+i-1] = i
                longest_motif = i
        if longest_motif < i:
            break
    return result


with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print(" ".join(map(str, failure_array(strand_array[0]))), file=file)
