# Connected Components
# http://rosalind.info/problems/cc/

from collections import defaultdict
from utilities import get_file, get_answer_file

def get_graph_dict(graph_arrays):
    neighbor = defaultdict(list)

    for i in graph_arrays:
        neighbor[i[0]].append(i[1])
        neighbor[i[1]].append(i[0])

    return neighbor


def get_BFS_visited_array(graph_dict, start):
    visited = []
    queue = [start]

    while len(queue) != 0:
        i = queue.pop(0)
        if i not in visited:
            visited.append(i)
            queue += graph_dict[i]
            queue = list(set(i for i in queue if i not in set(visited)))
    
    return visited


def get_components_count(size_of_graph, graph_dict):
    num_array = [i for i in range(1, size_of_graph+1)]
    components_count = 0

    while len(num_array) != 0:
        components_count += 1
        visited_array = get_BFS_visited_array(graph_dict, num_array[0])
        num_array = [i for i in num_array if i not in visited_array]

    return components_count


with get_file() as file:
    size_of_graph, len_of_input = map(int, file.readline().split())
    graph_arrays = []

    for line in file.readlines():
        graph_arrays.append(list(map(int, line.split())))  
    
    graph_dict = get_graph_dict(graph_arrays)

with get_answer_file() as file:
    print(get_components_count(size_of_graph, graph_dict), file=file)
