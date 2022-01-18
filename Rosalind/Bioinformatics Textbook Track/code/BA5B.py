# Find the Length of a Longest Path in a Manhattan-like Grid
# https://rosalind.info/problems/ba5b/

from utilities import get_file, get_answer_file

def MTP(n, m, down_matrix, right_matrix):
    cost = [[0]*(m+1) for _ in range(n+1)]
    cost[0][0] = 0
    for i in range(1, n+1):
        cost[i][0] = cost[i-1][0] + down_matrix[i-1][0]
    for j in range(1, m+1):
        cost[0][j] = cost[0][j-1] + right_matrix[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost[i][j] = max(cost[i-1][j] + down_matrix[i-1][j], cost[i][j-1] + right_matrix[i][j-1])

    return(cost[-1][-1])
    

def read_MTP(n, file):
    down_matrix = []
    right_matrix = []
    for _ in range(n):
        down_matrix.append(list(map(int, file.readline().split())))
    file.readline()
    for _ in range(n+1):
        right_matrix.append(list(map(int, file.readline().split())))
    return down_matrix, right_matrix

with get_file() as file:
    n, m = map(int, file.readline().split())
    down_matrix , right_matrix = read_MTP(n, file)

with get_answer_file() as file:
    print(MTP(n, m, down_matrix, right_matrix), file=file)