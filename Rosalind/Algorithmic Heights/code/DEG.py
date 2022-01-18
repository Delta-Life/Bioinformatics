# Degree Array
# http://rosalind.info/problems/deg/

from utilities import get_file, get_answer_file

def get_degree_of_graph(graph, max_vertices):
    degree = [0 for i in range(max_vertices)]
    for i in (i for j in graph for i in j):
        degree[i - 1] += 1
    return degree


with get_file() as file:
    max_vertices, len_of_input = map(int, file.readline().split())
    graph = []
    for line in file.readlines():
        graph.append(list(map(int, line.split())))

with get_answer_file() as file:
    degree = get_degree_of_graph(graph, max_vertices)
    print(" ".join(map(str, degree)), file=file)