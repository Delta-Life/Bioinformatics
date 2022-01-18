# Find a Longest Common Subsequence of Two Strings
# https://rosalind.info/problems/ba5c/

from utilities import get_file, get_answer_file

def LCS(str1, str2):
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j], cost[i][j-1], cost[i-1][j-1]+1 if str1[j-1]==str2[i-1] else cost[i-1][j-1])
    
    i = len(str2)
    j = len(str1)
    result = []
    while j * i != 0:
        if cost[i][j-1] == cost[i][j]:
            j -= 1
        elif cost[i-1][j] == cost[i][j]:
            i -= 1
        else:
            result.append(str1[j-1])
            j -= 1
            i -= 1
    return("".join(reversed(result)))


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    print(LCS(str1, str2), file=file)