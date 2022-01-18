# Counting Point Mutations
# http://rosalind.info/problems/hamm/

from utilities import get_file, get_answer_file

def count_mutations(strand1, strand2):
    return sum(i != j for i, j in zip(strand1, strand2))

with get_file() as file:
    strand1 = file.readline().rstrip()
    strand2 = file.readline().rstrip()

with get_answer_file() as file:
    print(count_mutations(strand1, strand2), file=file)