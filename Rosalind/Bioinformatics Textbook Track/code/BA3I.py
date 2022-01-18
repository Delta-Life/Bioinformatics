# Find a k-Universal Circular String
# https://rosalind.info/problems/ba3i/


from utilities import get_file, get_answer_file, get_de_bruijn, get_cycle
from itertools import product

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

def get_eulerian_cycle(graph, start=0):
    cycle = [start] + get_cycle(graph, start)
    updated = True
    while updated:
        updated = False
        for i, start in enumerate(cycle):
            if start in graph:
                updated = True
                cycle = cycle[:i+1] + get_cycle(graph, start) + cycle[i+1:]

    return cycle

def univ_circle(k):
    strings = ["".join(i) for i in product("01", repeat=k)]
    graph = get_de_bruijn(strings)
    path = get_eulerian_cycle(graph, start="0"*(k-1))

    return path[0] + "".join([path[i][-1] for i in range(1, len(path)-k+1)])


with get_file() as file:
    k = int(file.readline().rstrip())

with get_answer_file() as file:
    print("".join(univ_circle(k)), file=file)