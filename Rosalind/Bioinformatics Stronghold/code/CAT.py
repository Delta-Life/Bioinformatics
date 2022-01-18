# Catalan Numbers and RNA Secondary Structures
# http://rosalind.info/problems/cat/

from collections import defaultdict
from utilities import get_file, read_FASTA, get_answer_file

# Noncrosing Perfect Maching
def catalan(strand):
    if (strand not in cache):
        if strand.count('C') != strand.count('G') or strand.count('A') != strand.count('U'):
            cache[strand] = 0
        else:
            cache[strand] = sum([catalan(strand[1:i]) * cache[strand[0]+strand[i]] * catalan(strand[i+1:]) for i in range(1, len(strand), 2)])
    return cache[strand]

with get_file() as file:
    _, strand_array = read_FASTA(file)

with get_answer_file() as file:
    cache = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 'CG':1, 'CU':0,
             'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}
    NPM_num = catalan(strand_array[0])
    print(NPM_num % 1000000, file=file)
