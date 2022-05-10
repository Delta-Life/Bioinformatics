# Dijkstra's Algorithm
# https://rosalind.info/problems/dij/

from utilities import get_file, get_answer_file

def dij_search(V, adjacency_matrix):
    cost_array = [0] + [-1] * (V - 1)
    queue = [0]
    while queue != []:
        dept = queue.pop()
        for arri, cost in enumerate(adjacency_matrix[dept]):
            if cost != -1:
                if cost_array[arri] == -1 or cost_array[dept] + cost < cost_array[arri]:
                    cost_array[arri] = cost_array[dept] + cost
                    if arri not in queue:
                        queue.append(arri)
    return cost_array

with get_file() as file:
    V, E = map(int, file.readline().split())
    adjacency_matrix = [[-1] * V for _ in range(V)]
    for line in file.readlines():
        dept, arri, cost = map(int, line.split())
        adjacency_matrix[dept-1][arri-1] = cost

with get_answer_file() as file:
    print(" ".join(map(str, dij_search(V, adjacency_matrix))), file=file)