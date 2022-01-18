# Generate All Maximal Non-Branching Paths in a Graph
# https://rosalind.info/problems/ba3m/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_cycle(graph, indegree, start):
    cycle = [start]
    while sum([i == start for i in cycle]) != 2:
        for node in graph[cycle[-1]]:
            if indegree[node] == 1:
                indegree[node] -= 1
                cycle.append(node)

    return cycle

def get_toplogical_order(graph):
    queue = []
    result = []
    indegree = defaultdict(int)
    outdegree = defaultdict(int)

    for key, value in graph.items():
        indegree[key]
        for v in value:
            indegree[v] += 1
    
    for key, value in graph.items():
        outdegree[key] = len(value)
    
    for key, value in indegree.items():
        if value < outdegree[key]:
            queue.append(key)

    for key in queue:
        indegree[key] = 10**5

    while queue:
        tmp = queue.pop()
        for node in graph[tmp]:
            path = [tmp, node]
            indegree[path[-1]] -= 1
            while True:
                if len(graph[path[-1]]) == 1 and sum([path[-1] == v for value in graph.values() for v in value]) == 1:
                    outdegree[path[-1]] -= 1
                    path.append(graph[path[-1]][0])
                    indegree[path[-1]] -= 1
                elif len(graph[path[-1]]) == 0:
                    break
                else:
                    indegree[path[-1]] -= 1
                    break
            result.append(path)
        outdegree[tmp] = 0
        indegree[tmp] = 10 ** 8
        
        for key, value in indegree.items():
            if value < outdegree[key]:
                queue.append(key)
    
    for key, value in indegree.items():
        if indegree[key] == 1:
            result.append(get_cycle(graph, indegree, key))

    return [" -> ".join(map(str, i)) for i in result]

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
    print("\n".join(get_toplogical_order(graph)), file=file)