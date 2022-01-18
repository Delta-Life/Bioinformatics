# Overlap Graphs
# http://rosalind.info/problems/grph/

from utilities import get_file, read_FASTA, get_answer_file
from collections import defaultdict

def overlap_graphs(strand_array):
    left_dic = defaultdict(list)
    graph = []

    for n, i in enumerate(strand_array):
        left_dic[i[:3]].append(n)

    for n, i in enumerate(strand_array):
        tmp = left_dic[i[-3:]]
        for j in tmp:
            if n != j:
                graph.append([n, j])
    
    return graph

with get_file() as file:
    name_array, strand_array = read_FASTA(file)

with get_answer_file() as file:
    for graphs in overlap_graphs(strand_array):
        print(name_array[graphs[0]], name_array[graphs[1]], file=file)
