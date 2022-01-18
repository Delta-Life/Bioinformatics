# Compute Limb Lengths in a Tree
# https://rosalind.info/problems/ba7b/

from utilities import get_file, get_answer_file

def get_limb_length(distance, n, j):
	return min(distance[i][j] + distance[j][k] - distance[i][k]
		for i in range(n) for k in range(n) if i != j and k != j) // 2

with get_file() as file:
    n = int(file.readline().rstrip())
    node = int(file.readline().rstrip())
    distance = [line.split() for line in file.readlines()]
    for n, d in enumerate(distance):
         distance[n] = list(map(int, d))

with get_answer_file() as file:
    print(get_limb_length(distance, n, node), file=file)
    