# Breadth-First Search
# http://rosalind.info/problems/bfs/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_graph_dict(graph_arrays):
    neighbor = defaultdict(list)
    for i in graph_arrays:
        neighbor[i[0]].append(i[1])
    return neighbor

def get_degree_array(graph_dict):
    visited = []
    queue_array = [[1]]

    while len(queue_array[-1]) != 0:
        queue_array.append([])
        for i in queue_array[-2]:
            if i not in visited:
                visited.append(i)
                queue_array[-1] += graph_dict[i]
                queue_array[-1] = list(set(i for i in queue_array[-1] if i not in set(visited)))
    
    return queue_array


with get_file() as file:
    size_of_graph, len_of_input = map(int, file.readline().split())
    graph_arrays = []

    for line in file.readlines():
        graph_arrays.append(list(map(int, line.split())))  
    
    graph_dict = get_graph_dict(graph_arrays)

with get_answer_file() as file:
    queue_array = get_degree_array(graph_dict)
    for i in range(1, size_of_graph + 1):
        flag = True
        for n, j in enumerate(queue_array):
            if i in j:
                print(n, end=" ", file=file)
                flag = False
                break
        if flag:
            print("-1", end=" ", file=file)