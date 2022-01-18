# Find All Approximate Occurrences of a Pattern in a String
# https://rosalind.info/problems/ba1h/

from utilities import get_file, get_answer_file, hamming_distance

def approximate_pattern(pattern, strand, distance):
    len_s = len(strand)
    len_p = len(pattern)
    result = []
    for i in range(len_s-len_p+1):
        if hamming_distance(strand[i:i+len_p], pattern) <= distance:
            result.append(i)
    return result

with get_file() as file:
    pattern = file.readline().rstrip()
    strand = file.readline().rstrip()
    distance = int(file.readline().rstrip())

with get_answer_file() as file:
    print(" ".join(map(str, approximate_pattern(pattern, strand, distance))), file=file)