# Compute Distances Between Leaves
# https://rosalind.info/problems/ba7a/

from utilities import get_file, get_answer_file, read_weighted_graph

# Floyd–Warshall algorithm
def distance_between_leaves(graph, cost_dict, n):
    distance = [[10**9]*(max(graph.keys())+1) for _ in range(max(graph.keys())+1)]
    for key, value in graph.items():
        distance[key][key] = 0
        for v in value:
            print(v, value, value.index(v))
            distance[key][v] = cost_dict[key][value.index(v)]
    for c in distance:
        print(c)
    for k in range(max(graph.keys())+1):
        for i in range(max(graph.keys())+1):
            for j in range(max(graph.keys())+1):
                if distance[i][j] >  distance[i][k] +  distance[k][j]:
                     distance[i][j] =  distance[i][k] +  distance[k][j]
    
    return  distance[:n]



with get_file() as file:
    n = int(file.readline().rstrip())
    graph, cost_dict = read_weighted_graph(file)

with get_answer_file() as file:
    for c in distance_between_leaves(graph, cost_dict, n):
        print(" ".join(map(str, c[:n])), file=file)