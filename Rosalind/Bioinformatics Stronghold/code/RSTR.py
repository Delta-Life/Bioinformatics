# Matching Random Motifs
# https://rosalind.info/problems/rstr/

from utilities import get_file, get_answer_file

def get_motif_prob(length, gc_content, strand):
    prob_dict = {'G':gc_content/2, 'C':gc_content/2, 'A':(1-gc_content)/2, 'T':(1-gc_content)/2}
    prob = 1

    for i in strand:
        prob *= prob_dict[i]
    
    return 1 - (1 - prob) ** (length - len(strand) + 1)

with get_file() as file:
    length, gc_content = file.readline().split()
    length = int(length)
    gc_content = float(gc_content)
    strand = file.readline().rstrip()

with get_answer_file() as file:
    print(get_motif_prob(length, gc_content, strand), file=file)