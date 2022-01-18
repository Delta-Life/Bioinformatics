# Compute the Hamming Distance Between Two Strings
# https://rosalind.info/problems/ba1g/

from utilities import get_file, get_answer_file

def hamming_distance(s1, s2):
    return sum([i != j for i,j in zip(s1, s2)])

with get_file() as file:
    strand1 = file.readline().rstrip()
    strand2 = file.readline().rstrip()

with get_answer_file() as file:
    print(hamming_distance(strand1, strand2), file=file)