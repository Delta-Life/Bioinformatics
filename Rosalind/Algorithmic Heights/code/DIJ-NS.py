# Dijkstra's Algorithm
# http://rosalind.info/problems/dij/

from utilities import get_file, get_answer_file
from collections import defaultdict

def get_min_cost(num, graph_dict, cost_dict):
    visited = [1]
    queue = []
    for i in graph_dict[1]:
        queue.append(i)
    min_cost = []
    

with get_file() as file:
    num, _ = map(int, file.readline().split())
    graph_dict = defaultdict(list)
    cost_dict = defaultdict(list)

    for line in file.readlines():
        start, end, cost = map(int, line.split())
        graph_dict[start].append(end)
        cost_dict[start].append(cost)

with get_answer_file() as file:
    get_min_cost(num, graph_dict, cost_dict)
    print()