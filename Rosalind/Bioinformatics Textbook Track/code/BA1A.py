# Compute the Number of Times a Pattern Appears in a Text
# https://rosalind.info/problems/ba1a/

from utilities import get_file, get_answer_file

def count_pattern(pattern, strand):
    count = 0
    for i in range(len(strand) - len(pattern) + 1):
        if strand[i:i+len(pattern)] == pattern:
            count += 1
    return count

with get_file() as file:
    strand = file.readline().rstrip()
    pattern = file.readline().rstrip()

with get_answer_file() as file:
    print(count_pattern(pattern, strand), file=file)