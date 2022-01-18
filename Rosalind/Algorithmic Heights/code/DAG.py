# Testing Bipartiteness
# http://rosalind.info/problems/bip/

from collections import defaultdict
from utilities import get_file, get_answer_file

def read_graph(num_of_graphs, file):
    graph_arrays = [[]]
    size_array = []
    file.readline()
    for i in range(num_of_graphs):
        size, len_of_input = map(int, file.readline().split())
        size_array.append(size)
        for j in range(len_of_input):
            graph_arrays[i].append(list(map(int, file.readline().split())))
        file.readline()
        graph_arrays.append([])
    return graph_arrays, size_array

def get_graph_dict(graph_array):
    neighbor = defaultdict(list)
    for i in graph_array:
        neighbor[i[0]].append(i[1])
    return neighbor

def is_cycle(size, graph_array):
    graph_dict = get_graph_dict(graph_array)

    for i in range(1, size+1):
        visited = []
        stack = [i]
        while len(stack) != 0:
            vertex = stack.pop(-1)
            visited.append(vertex)
            for j in graph_dict[vertex]:
                if j not in visited:
                    stack = list(set(stack + [j]))
                else:
                    tmp = graph_dict[j]
                    while len(tmp) != 0:
                        tmp_vertex = tmp.pop(-1)
                        for k in graph_dict[tmp_vertex]:
                            if k == j:
                                return -1
                            elif k in visited:
                                tmp = list(set(tmp + [k]))
    return 1

with get_file() as file:
    num_of_graphs = int(file.readline().rstrip())
    graph_arrays, size_array = read_graph(num_of_graphs, file)

with get_answer_file() as file:
    for i, j in zip(size_array, graph_arrays[:-1]):
        print(is_cycle(i, j), end=" ", file=file)