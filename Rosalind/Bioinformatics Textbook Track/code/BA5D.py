# Find the Longest Path in a DAG
# https://rosalind.info/problems/ba5d/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_longest_path(graph, cost_graph, start, end):
    max_path = [end]
    visited = [start]
    visited_cost = [0]
    queue = [i for i in graph[start]]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
            for n, visited_node in enumerate(visited):
                if node in graph[visited_node]:
                    index = graph[visited_node].index(node)
                    visited_cost.append(visited_cost[n] + cost_graph[visited_node][index])
                    break
        else:
            indexes = []
            costs = []
            for n, visited_node in enumerate(visited):
                if node in graph[visited_node]:
                    indexes.append(n)
            for i in indexes:
                index = graph[visited[i]].index(node)
                costs.append(visited_cost[i] + cost_graph[visited[i]][index])
            index = visited.index(node)
            visited_cost[index] = max(costs)
            for i, cost in zip(indexes, costs):
                if cost != max(costs):
                    index = graph[visited[i]].index(node)
                    graph[visited[i]].pop(index)
                    cost_graph[visited[i]].pop(index)
    
    index = visited.index(end)
    while start not in max_path:
        for node in visited:
            if max_path[-1] in graph[node]:
                max_path.append(node)
                break
    
    return reversed(max_path), visited_cost[index]

def read_weighted_graph(file):
    graph = defaultdict(list)
    cost_graph = defaultdict(list)
    for i in file.readlines():
        start, ends= i.rstrip().split("->")
        ends, costs = ends.split(":")
        for j in ends.split(","):
            graph[int(start)].append(int(j))
        for j in costs.split(","):
            cost_graph[int(start)].append(int(j))

    return graph, cost_graph

with get_file() as file:
    start = int(file.readline().rstrip())
    end = int(file.readline().rstrip())
    graph, cost_graph = read_weighted_graph(file)


with get_answer_file() as file:
    path, cost = get_longest_path(graph, cost_graph, start, end)
    print(cost, file=file)
    print("->".join(map(str, path)), file=file)
