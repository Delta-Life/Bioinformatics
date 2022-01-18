# Implement AdditivePhylogeny
# https://rosalind.info/problems/ba7c/

from utilities import get_file, get_answer_file, get_limb_length

def get_path(graph, src, dst, visited):
    visited[src] = True
    for v, w in graph[src]:
        if visited[v]:
            continue
        if v == dst:
            return[(src, w), (dst, 0)]
        path = get_path(graph, v, dst, visited)
        if path is not None:
            return [(src, w)] + path
    return None

def delete_edge(graph, src, dst):
    for i, (neighbor, _) in enumerate(graph[src]):
        if neighbor == dst:
            break
    del graph[src][i]

    for i, (neighbor, _) in enumerate(graph[dst]):
        if neighbor == src:
            break
    del graph[dst][i]

def insert_new_node(graph, src, dst, d, visited, node):
    path = get_path(graph, src, dst, visited)
    print(path, "!!")
    curr = 0
    edge_length = path[0][1]
    remaining_length = d

    while remaining_length >= edge_length:
        remaining_length -= edge_length
        curr += 1
        edge_length = path[curr][1]
    
    curr_node = path[curr][0]
    next_node = path[curr+1][0]
    print(graph)
    print(curr_node, "Cur")
    print(next_node, "nex")

    graph[curr_node].append((node, remaining_length))
    graph[next_node].append((node, edge_length - remaining_length))
    graph[node] = [(curr_node, remaining_length), (next_node, edge_length - remaining_length)]
    print(graph)

    delete_edge(graph, curr_node, next_node)

def additive_phylogeny(distance, n):
    def phylogeny(n, node):
        if n == 2:
            return {0:[(1, distance[0][1])], 1:[(0, distance[0][1])]}
        limb_length = get_limb_length(distance, n, n-1)
        print(limb_length)
        for i in range(n-1):
            distance[i][n-1] -= limb_length
            distance[n-1][i] -= limb_length
        for i in range(n-1):
            for j in range(i+1, n-1):
                if distance[i][j] == distance[i][n-1] + distance[j][n-1]:
                    d = distance[i][n-1]
                    src, dst = i, j
                    break
        graph = phylogeny(n-1, node-1)
        print(src, dst)
        print(graph)
        visited = [False] * (2 * len(distance))
        insert_new_node(graph, src, dst, d, visited, node)
        graph[n-1] = [(node, limb_length)]
        graph[node].append((n-1, limb_length))
        return graph
    
    return phylogeny(n+1, node=2*len(distance)-3)

with get_file() as file:
    n = int(file.readline().rstrip())
    distance = [line.split() for line in file.readlines()]
    for n, d in enumerate(distance):
        distance[n] = list(map(int, d))

with get_answer_file() as file:
    graph = additive_phylogeny(distance, n)
    for src in graph:
        for dst, length in graph[src]:
            print("{0}->{1}:{2}".format(src, dst, length), file=file)