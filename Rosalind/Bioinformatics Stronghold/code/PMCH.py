# Perfect Matchings and RNA Secondary Structures
# http://rosalind.info/problems/pmch/

from utilities import get_file, read_FASTA, factor, get_answer_file

def get_perfect_matching_num(strand):
    return factor(strand.count('A')) * factor(strand.count('G'))

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    perfect_matching_num = get_perfect_matching_num(strand_array[0])
    print(perfect_matching_num, file=file)
