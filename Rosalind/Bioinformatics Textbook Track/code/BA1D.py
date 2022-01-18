# Find All Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1d/

from utilities import get_file, get_answer_file

def index_pattern(pattern, strand):
    index = []
    for i in range(len(strand)):
        if strand[i:i+len(pattern)] == pattern:
            index.append(i)
    return index

with get_file() as file:
    pattern = file.readline().rstrip()
    strand = file.readline().rstrip()

with get_answer_file() as file:
    print(" ".join(map(str, index_pattern(pattern, strand))), file=file)