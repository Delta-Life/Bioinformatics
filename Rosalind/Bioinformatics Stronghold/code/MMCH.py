# Maximum Matchings and RNA Secondary Structures
# https://rosalind.info/problems/mmch/

from utilities import get_file, get_answer_file, read_FASTA, factor

def get_maximum_matching(strand):
    a = strand.count('A')
    u = strand.count('U')
    g = strand.count('G')
    c = strand.count('C')

    if a > u:
        au = factor(a)//factor(a-u)
    else:
        au = factor(u)//factor(u-a)
    if c > g:
        gc = factor(c)//factor(c-g)
    else:
        gc = factor(g)//factor(g-c)
    
    return au*gc

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    print(get_maximum_matching(strand_array[0]), file=file)