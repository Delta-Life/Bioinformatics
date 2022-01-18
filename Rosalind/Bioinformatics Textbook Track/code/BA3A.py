# Generate the k-mer Composition of a String
# https://rosalind.info/problems/ba3a/

from utilities import get_file, get_answer_file

def k_mer(k, strand):
    for i in range(len(strand)-k+1):
        yield strand[i:i+k]

with get_file() as file:
    k = int(file.readline().rstrip())
    strand = file.readline().rstrip()

with get_answer_file() as file:
    for i in k_mer(k, strand):
        print(i, file=file)