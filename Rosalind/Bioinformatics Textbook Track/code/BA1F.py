# Find Patterns Forming Clumps in a String
# https://rosalind.info/problems/ba1e/

from utilities import get_file, get_answer_file

def index_min_skew(strand):
    skew_strand = []
    for i in strand:
        if i == 'G':
            skew_strand.append(1)
        elif i == 'C':
            skew_strand.append(-1)
        else:
            skew_strand.append(0)
    skew_array = [sum(skew_strand[i:]) for i in range(len(skew_strand))]
    return [n for n, i in enumerate(skew_array) if i == max(skew_array)]

with get_file() as file:
    strand = file.readline().rstrip()

with get_answer_file() as file:
    print(" ".join(map(str, index_min_skew(strand))), file=file)