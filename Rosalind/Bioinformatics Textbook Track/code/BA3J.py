# Reconstruct a String from its Paired Composition
# https://rosalind.info/problems/ba3j/

from collections import defaultdict
from utilities import get_file, get_answer_file, get_cycle, get_cycle_with_end

def read_pairs(file):
    kmer_dict = defaultdict(list)
    strand_pairs = [line.rstrip().split("|") for line in file.readlines()]
    k = len(strand_pairs[0][0])-1
    
    for strand_pair in strand_pairs:
        kmer_dict[strand_pair[0][:k], strand_pair[1][:k]].append(tuple([strand_pair[0][-k:], strand_pair[1][-k:]]))

    return kmer_dict

def reconstruct_strand(graph, k, d):
    end = 0
    for edges in graph.values():
        for edge in edges:
            if edge not in graph.keys():
                end = edge
    graph[end] = []

    start = 0
    for i in graph.keys():
        if len(graph[i]) != sum(i in edges for edges in graph.values()):
            if len(graph[i]) < sum(i in edges for edges in graph.values()):
                end = i
            else:
                start = i
    graph[end] = [start]

    cycle = get_cycle_with_end(graph, start, end)
    updated = True
    while updated:
        updated = False
        for i, start in enumerate(cycle):
            if start in graph:
                updated = True
                least_cycle = get_cycle(graph, start)
                cycle = cycle[:i+1] + least_cycle + cycle[i+1:]
                break
    return cycle[0][0] + "".join([cycle[i][0][-1] for i in range(1,len(cycle))]) + "".join([cycle[i][1][-1] for i in range(len(cycle)-k-d, len(cycle))])


with get_file() as file:
    k, d = map(int, file.readline().split())
    graphs = read_pairs(file)

with get_answer_file() as file:
    print(reconstruct_strand(graphs, k, d), file=file)