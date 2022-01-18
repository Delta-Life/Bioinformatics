# Double-Degree Array
# http://rosalind.info/problems/ddeg/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_graph_dict(graph_arrays):
    neighbor = defaultdict(list)
    for i in graph_arrays:
        neighbor[i[0]].append(i[1])
        neighbor[i[1]].append(i[0])
    return neighbor

with get_file() as file:
    max_vertices, len_of_input = map(int, file.readline().split())
    graph_arrays = []
    for line in file.readlines():
        graph_arrays.append(list(map(int, line.split())))  

with get_answer_file() as file:
    neighbor = get_graph_dict(graph_arrays)
    for i in range(1, max_vertices + 1):
        print(sum([len(neighbor[j]) for j in neighbor[i]]), end=" ", file=file)