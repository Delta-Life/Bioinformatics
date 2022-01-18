# Find an Eulerian Cycle in a Graph
# https://rosalind.info/problems/ba3f/

from utilities import get_file, get_answer_file
from collections import defaultdict

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

def get_eulerian_cycle(graph, start=0):
    least_cycle = [start] + get_cycle(graph, start)
    cycle = least_cycle
    updated = True
    while updated:
        updated = False
        for i, start in enumerate(least_cycle):
            if start in graph:
                updated = True
                least_cycle = get_cycle(graph, start)
                cycle = cycle[:i+1] + least_cycle + cycle[i+1:]

    return cycle

def read_graph(file):
    graph = defaultdict(list)
    for i in file.readlines():
        start , ends= i.rstrip().split(" -> ")
        for j in ends.split(","):
            graph[int(start)].append(int(j))

    return graph

with get_file() as file:
    graph = read_graph(file)

with get_answer_file() as file:
    print("->".join(map(str, get_eulerian_cycle(graph))), file=file)