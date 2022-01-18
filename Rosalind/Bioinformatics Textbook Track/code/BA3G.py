# Find an Eulerian Path in a Graph
# https://rosalind.info/problems/ba3g/

from utilities import get_file, get_answer_file, get_cycle, read_graph

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

def get_eulerian_path(graph):
    
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
    return cycle

with get_file() as file:
    graph = read_graph(file)

with get_answer_file() as file:
    print("->".join(map(str, get_eulerian_path(graph))), file=file)