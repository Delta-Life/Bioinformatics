# Inferring mRNA from Protein
# http://rosalind.info/problems/mrna/

from utilities import get_file, get_codon_table, read_all
from collections import Counter

def reverse_translation_num(protein_string , modulo):
    codon_table = get_codon_table()
    codon_num = Counter(codon_table[i][1] for i in range(len(codon_table)))
    total_num = 1
    cal_translation = lambda total_num, codon_num: total_num * codon_num % modulo

    for amino_acid in protein_string:
        total_num = cal_translation(total_num, codon_num[amino_acid])
    
    return total_num * codon_num["Stop"]


with get_file() as file:
    protein_string = read_all(file)

print(reverse_translation_num(protein_string, 1000000))