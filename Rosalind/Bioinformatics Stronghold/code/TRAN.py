# Transitions and Transversions
# http://rosalind.info/problems/tran/

from utilities import get_file, read_FASTA, get_answer_file

def count_transition(strand1, strand2):
    transition_dict = {'A':'G', 'C':'T', 'G':'A', 'T':'C'}
    count = 0
    for i, j in zip(strand1, strand2):
        if transition_dict[i] == j:
            count += 1
    
    return count

def count_transversion(strand1, strand2):
    transition_dict = {'A':['C', 'T'], 'G':['C', 'T'], 'T':['A', 'G'], 'C':['A', 'G']}
    count = 0
    for i, j in zip(strand1, strand2):
        if j in transition_dict[i]:
            count += 1
    
    return count


with get_file() as file:
    name_array, strand_array = read_FASTA(file)

with get_answer_file() as file:
    transition = count_transition(strand_array[0], strand_array[1])
    transversion = count_transversion(strand_array[0], strand_array[1])
    print(transition/transversion, file=file)
