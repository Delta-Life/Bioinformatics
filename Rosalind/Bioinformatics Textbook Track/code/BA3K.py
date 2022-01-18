# Generate Contigs from a Collection of Reads
# https://rosalind.info/problems/ba3k/

from collections import defaultdict
from utilities import get_file, get_answer_file, get_de_bruijn

def get_contigs(graph):
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
    
    for i in range(len(result)):
        result[i] = result[i][0] + "".join(result[i][j][-1] for j in range(1, len(result[i])))

    return sorted(result)

with get_file() as file:
    strand_array = [line.rstrip() for line in file.readlines()]
    graph = get_de_bruijn(strand_array)
    print(graph)

with get_answer_file() as file:
    print(" ".join(get_contigs(graph)), file=file)