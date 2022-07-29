'''
codes of common fuctions

list:
cyclospectrum
get_amino_acid_mass_dict
get_answer_file
get_complement_strand
get_cycle
get_cycle_with_end
get_de_bruijn
get_file
get_limb_length
get_profile
hamming_distance
read_graph
read_weighted_graph
score
'''

import sys
from collections import defaultdict
from itertools import combinations

def cyclospectrum(peptide):
    tmp = peptide + peptide
    amino_mass_dict = get_amino_acid_mass_dict()
    cyclospectrum = []
    cyclosubs = ['', peptide]
    for i, j in combinations(range(0, len(peptide)), 2):
        cyclosubs.append(tmp[i:j])
    for i, j in combinations(range(0, len(tmp)), 2):
        if j-i < len(peptide) and j>len(peptide)-1 and len(peptide)>i:
            cyclosubs.append(tmp[i:j])
    for peptide in list(cyclosubs):
        sum = 0
        for amino_acid in peptide:
            sum += amino_mass_dict[amino_acid]
        cyclospectrum.append(sum)

    return sorted(cyclospectrum)

def get_amino_acid_mass_dict(): 
    array = ["G 57", "A 71", "S 87", "P 97", "V 99", "T 101", "C 103", "I 113", "L 113", "N 114", "D 115", "K 128", "Q 128", "E 129", "M 131", "H 137", "F 147", "R 156", "Y 163", "W 186"]
    array = [i.split() for i in array]
    return {i:int(j) for i, j in array}

def get_answer_file():
    filePath = sys.argv[0].split("/")
    return open("/".join(filePath[:-1]) + "/../answer/rosalind_" + filePath[-1].split(".")[0].lower() + ".txt", 'w')

def get_complement_strand(strand):
    translator = str.maketrans("ATGC", "TACG")
    return strand[::-1].translate(translator)

def get_cycle(graph, start):
    cycle = []
    u = graph[start].pop()
    while u != start:
        cycle.append(u)
        u = graph[u].pop()
    cycle.append(u)
    
    toRemove = [k for k, v in graph.items() if not v]
    for k in toRemove:
        del graph[k]

    return cycle

def get_cycle_with_end(graph, start, end):
    cycle = [end]
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    while start not in cycle:
        for node in visited:
            if cycle[-1] in graph[node]:    
                graph[node].remove(cycle[-1])
                cycle.append(node)
                break
    graph[end].remove(start)
    toRemove = [k for k, v in graph.items() if not v]
    for k in toRemove:
        del graph[k]
    cycle.reverse()
    return cycle

def get_de_bruijn(strand_array):
    kmer_dict = defaultdict(list)
    k = len(strand_array[0])-1
    
    for i in strand_array:
        kmer_dict[i[:k]].append(i[-k:])

    return kmer_dict

def get_file():
    filePath = sys.argv[0].split("/")
    return open("/".join(filePath[:-1]) + "/../data/rosalind_" + filePath[-1].split(".")[0].lower() + ".txt", 'r')

def get_limb_length(distance, n, j):
	return min(distance[i][j] + distance[j][k] - distance[i][k]
		for i in range(n) for k in range(n) if i != j and k != j) // 2

def get_motif(profile, strand, k):
    nucleo_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    seq = {}
    for j in range(len(strand)-k+1):
        prob = 1
        for n, nucleo in enumerate(strand[j:j+k]):
            prob *= profile[nucleo_dict[nucleo]][n]
        seq[strand[j:j+k]] = prob
    return sorted(seq.items(), key=lambda x:x[1], reverse=True)[0][0]

def get_profile(strand_array, k):
    nucleo_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = [[0] * k for _ in range(4)]
    for j in range(k):
        for strand in strand_array:
            profile[nucleo_dict[strand[j]]][j] += 1
    return profile

def get_profile_pseudocounts(strand_array, k):
    nucleo_dict = {'A':0, 'C':1, 'G':2, 'T':3}
    profile = [[1] * k for _ in range(4)]
    for j in range(k):
        for strand in strand_array:
            profile[nucleo_dict[strand[j]]][j] += 1
    return profile

def hamming_distance(s1, s2):
    return sum([i != j for i,j in zip(s1, s2)])

def load_blosum62():
    BLOSUM62 = [" 4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2",
        "0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2",
        "-2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3",
        "-1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2",
        "-2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3",
        "0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3",
        "-2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2",
        "-1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1",
        "-1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2",
        "-1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1",
        "-1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1",
        "-2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2",
        "-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3",
        "-1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1",
        "-1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2",
        " 1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2",
        " 0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2",
        " 0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1",
        "-3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2",
        "-2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7"]
    for n, cost in enumerate(BLOSUM62):
        BLOSUM62[n] = list(map(int, cost.split()))
    return BLOSUM62

def load_pam250():
    PAM250 = [" 2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3",
        "-2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0",
        " 0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4",
        " 0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4",
        "-3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7",
        " 1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5",
        "-1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0",
        "-1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1",
        "-1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4",
        "-2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1",
        "-1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2",
        " 0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2",
        " 1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5",
        " 0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4",
        "-2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4",
        " 1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3",
        " 1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3",
        " 0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2",
        "-6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0",
        "-3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10"]
    for n, cost in enumerate(PAM250):
        PAM250[n] = list(map(int, cost.split()))
    return PAM250

def load_protein_dictionary():
    return {i:n for n, i in enumerate("A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y".split())}

def read_graph(file):
    graph = defaultdict(list)
    for i in file.readlines():
        start , ends= i.rstrip().split(" -> ")
        for j in ends.split(","):
            graph[int(start)].append(int(j))
    return graph

def read_weighted_graph(file):
    graph = defaultdict(list)
    cost_graph = defaultdict(list)
    for i in file.readlines():
        start, ends= i.rstrip().split("->")
        ends, costs = ends.split(":")
        for j in ends.split(","):
            graph[int(start)].append(int(j))
        for j in costs.split(","):
            cost_graph[int(start)].append(int(j))
    
    return graph, cost_graph


def score(Motifs):
    score = 0
    for i in range(len(Motifs[0])):
        j = [motif[i] for motif in Motifs]
        score += (len(j) - max(j.count("A"), j.count("C"), j.count("T"), j.count("G")))
    return score