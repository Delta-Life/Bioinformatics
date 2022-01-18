#  Implement GreedyMotifSearch
#  https://rosalind.info/problems/ba2d/

from utilities import get_file, get_answer_file

def get_profile(strand_array, k):
    nucleo_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = [[0] * k for _ in range(4)]
    for j in range(k):
        for strand in strand_array:
            profile[nucleo_dict[strand[j]]][j] += 1
    return profile

def get_motif(profile, strand, k):
    nucleo_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    seq = {}
    for j in range(len(strand)-k+1):
        prob = 1
        for n, nucleo in enumerate(strand[j:j+k]):
            prob *= profile[nucleo_dict[nucleo]][n]
        seq[strand[j:j+k]] = prob
    return sorted(seq.items(), key=lambda x:x[1], reverse=True)[0][0]

def score(Motifs):
    score = 0
    for i in range(len(Motifs[0])):
        j = [motif[i] for motif in Motifs]
        score += (len(j) - max(j.count("A"), j.count("C"), j.count("T"), j.count("G")))
    return score

def greedy_motif_search(strand_array, k, t):
    best_motifs = [strand[:k] for strand in strand_array]
    for k_mer in [strand_array[0][i:i+k] for i in range(len(strand_array[0])-k+1)]:
        motifs = [k_mer]
        for i in range(1, t):
            profile = get_profile(motifs, k)
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
    print("\n".join(greedy_motif_search(strand_array, k, t)), file=file)