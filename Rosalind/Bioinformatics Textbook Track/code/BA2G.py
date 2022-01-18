#  Implement GibbsSampler
#  https://rosalind.info/problems/ba2g/

from random import randint
from copy import deepcopy
from utilities import get_file, get_answer_file, get_profile_pseudocounts, get_motif, score

def gibbs_sampler(strand_array, k, t, n):
    best_motifs = []
    for i in range(t):
        index = randint(0, len(strand_array[0])-k)
        best_motifs.append(strand_array[i][index:index+k])
    for j in range(0, n):
        motifs = deepcopy(best_motifs)
        i = randint(0, t-1)
        motifs.pop(i)
        profile = get_profile_pseudocounts(motifs, k)
        motifs.insert(i, get_motif(profile, strand_array[i], k))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


with get_file() as file:
    k, t, n = map(int, file.readline().split())
    strand_array = []
    for i in file.readlines():
        strand_array.append(i.rstrip())

with get_answer_file() as file:
    best_motifs = gibbs_sampler(strand_array, k, t, n)
    for i in range(20):
        motifs = gibbs_sampler(strand_array, k, t, n)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    print("\n".join(best_motifs), file=file)