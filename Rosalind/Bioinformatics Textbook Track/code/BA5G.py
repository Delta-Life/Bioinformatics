# Compute the Edit Distance Between Two Strings
# https://rosalind.info/problems/ba5g/

from utilities import get_file, get_answer_file

def edit_distance(str1, str2):
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    matches = [[1]*(len(str1)) for _ in range(len(str2))]
    for i in range(len(cost)):
        cost[i][0] = 1 * i
    for i in range(len(cost[0])):
        cost[0][i] = 1 * i
    for i in range(len(matches)):
        for j in range(len(matches[0])):
            if str1[j] == str2[i]:
                matches[i][j] = 0
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = min(cost[i-1][j]+1, cost[i][j-1]+1, cost[i-1][j-1]+matches[i-1][j-1])
    return cost[-1][-1]


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    print(edit_distance(str1, str2), file=file)