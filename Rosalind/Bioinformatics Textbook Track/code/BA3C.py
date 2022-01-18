# Construct the Overlap Graph of a Collection of k-mers
# https://rosalind.info/problems/ba3c/

from utilities import get_file, get_answer_file
from collections import defaultdict

def overlap_graphs(strand_array):
    left_dic = defaultdict(list)
    graph = []
    k = len(strand_array[0]) - 1

    for n, i in enumerate(strand_array):
        left_dic[i[:k]].append(n)

    for n, i in enumerate(strand_array):
        tmp = left_dic[i[-k:]]
        for j in tmp:
            if n != j:
                graph.append([n, j])
    
    return graph

with get_file() as file:
    strand_array = [i.rstrip() for i in file.readlines()]

with get_answer_file() as file:
    for graphs in overlap_graphs(strand_array):
        print(strand_array[graphs[0]], "->", strand_array[graphs[1]], file=file)