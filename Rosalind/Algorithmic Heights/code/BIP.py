# Testing Bipartiteness
# http://rosalind.info/problems/bip/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_graph_dict(graph_array):
    neighbor = defaultdict(list)
    for i in graph_array:
        neighbor[i[0]].append(i[1])
        neighbor[i[1]].append(i[0])
    return neighbor

def test_bip(graph_array):
    graph_dict = get_graph_dict(graph_array)
    visited = []
    queue_array = [[1]]
    node1 = []
    node2 = []

    while len(queue_array[-1]) != 0:
        queue_array.append([])
        for i in queue_array[-2]:
            if i not in visited:
                visited.append(i)
                queue_array[-1] += graph_dict[i]
                for j in graph_dict[i]:
                    if len(queue_array) % 2 == 0:
                        node1.append(j)
                    else:
                        node2.append(j)
                queue_array[-1] = list(set(i for i in queue_array[-1] if i not in set(visited)))

    for i in visited:
        if i in node1 and i in node2:
            return -1
    return 1

with get_file() as file:
    num_of_graphs = int(file.readline().rstrip())
    graph_arrays = [[]]
    file.readline()
    for i in range(num_of_graphs):
        _, len_of_input = map(int, file.readline().split())
        for j in range(len_of_input):
            graph_arrays[i].append(list(map(int, file.readline().split())))
        file.readline()
        graph_arrays.append([])
    
with get_answer_file() as file:
    for i in range(num_of_graphs):
        print(test_bip(graph_arrays[i]), end=" ", file=file)