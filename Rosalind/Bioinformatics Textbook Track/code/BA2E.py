#  Implement GreedyMotifSearch with Pseudocounts
#  https://rosalind.info/problems/ba2e/

from utilities import get_file, get_answer_file, get_motif, get_profile_pseudocounts, score

def greedy_motif_search_pseudocounts(strand_array, k, t):
    best_motifs = [strand[:k] for strand in strand_array]
    for k_mer in [strand_array[0][i:i+k] for i in range(len(strand_array[0])-k+1)]:
        motifs = [k_mer]
        for i in range(1, t):
            profile = get_profile_pseudocounts(motifs, k)
            motifs.append(get_motif(profile, strand_array[i], k))


        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs

with get_file() as file:
    k, t = map(int, file.readline().split())
    strand_array = []
    for i in file.readlines():
        strand_array.append(i.rstrip())

with get_answer_file() as file:
    print("\n".join(greedy_motif_search_pseudocounts(strand_array, k, t)), file=file)