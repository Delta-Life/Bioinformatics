# Find a Topological Ordering of a DAG
# https://rosalind.info/problems/ba5n/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_toplogical_order(graph):
    queue = []
    result = []
    indegree = defaultdict(int)
    for key, value in graph.items():
        indegree[key]
        for v in value:
            indegree[v] += 1
    for key, value in indegree.items():
        if value < len(graph[key]):
            queue.append(key)

    for key in queue:
        del indegree[key]

    while queue:
        tmp = queue.pop()
        result.append(tmp)
        for key in graph[tmp]:
            indegree[key] -= 1
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        for key in queue:
            if indegree[key] == 0:
                del indegree[key]
    
    return result

def read_graph(file):
    graph = defaultdict(list)
    for i in file.readlines():
        start, ends= i.rstrip().split(" -> ")
        for j in ends.split(","):
            graph[int(start)].append(int(j))

    return graph

with get_file() as file:
    graph = read_graph(file)

with get_answer_file() as file:
    print(", ".join(map(str, get_toplogical_order(graph))), file=file)
