# Motzkin Numbers and RNA Secondary Structures
# https://rosalind.info/problems/motz/

from utilities import get_file, read_FASTA, get_answer_file

def get_motz_num(strand):
    table = {'AU': 2, 'UA': 2, 'GC': 2, 'CG': 2, 'A': 1, 'U': 1, 'G': 1, 'C': 1, '':1}
    def motz(strand):
        if strand not in table:
            p = motz(strand[1:])
            for i in range(1, len(strand)):
                if (strand[0] + strand[i]) in ['AU', 'UA', 'GC', 'CG']:
                    p += motz(strand[1:i]) * motz(strand[i+1:])
            table[strand] =  p % 1000000
        return table[strand]
    return motz(strand)

with get_file() as file:
    _, strand_array = read_FASTA(file)
    strand = strand_array[0]

with get_answer_file() as file:
    print(get_motz_num(strand), file=file)