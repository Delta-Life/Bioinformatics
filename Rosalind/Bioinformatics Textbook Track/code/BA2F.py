#  Implement RandomizedMotifSearch
#  https://rosalind.info/problems/ba2f/

from random import randint
from utilities import get_file, get_answer_file, get_profile_pseudocounts, get_motif, score

def randomized_motif_search(strand_array, k, t):
    best_motifs = []
    for i in range(t):
        index = randint(0, len(strand_array[0])-k)
        best_motifs.append(strand_array[i][index:index+k])
    while True:
        profile = get_profile_pseudocounts(best_motifs, k)
        motifs = []
        for strand in strand_array:
            motifs.append(get_motif(profile, strand, k))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


with get_file() as file:
    k, t = map(int, file.readline().split())
    strand_array = []
    for i in file.readlines():
        strand_array.append(i.rstrip())

with get_answer_file() as file:
    best_motifs = randomized_motif_search(strand_array, k, t)
    for i in range(1000):
        motifs = randomized_motif_search(strand_array, k, t)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    print("\n".join(best_motifs), file=file)