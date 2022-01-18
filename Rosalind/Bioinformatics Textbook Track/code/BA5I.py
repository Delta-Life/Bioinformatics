# Find a Highest-Scoring Overlap Alignment of Two Strings
# https://rosalind.info/problems/ba5i/

from utilities import get_file, get_answer_file

def get_fitting_alighment(str1, str2, penalty):
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(cost)):
        cost[i][0] = -penalty * i
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j]-penalty, cost[i][j-1]-penalty, cost[i-1][j-1]+1 if str1[j-1]==str2[i-1] else cost[i-1][j-1]-penalty)
    indexes = []
    max_cost = 0
    for n, c in enumerate(cost):
        if c[-1] > max_cost:
            max_cost = c[-1]
            indexes = [n]
        elif c[-1] == max_cost:
            indexes.append(n)
    max_result = [[], []]
    for i in indexes:
        j=len(str1)
        result = [[], []]
        while i != 0:
            if cost[i-1][j-1] + 1 == cost[i][j] and str1[j-1] == str2[i-1]:
                j -= 1
                i -= 1
                result[0].append(str1[j])
                result[1].append(str2[i])
            elif cost[i-1][j-1] -penalty == cost[i][j]:
                i -= 1
                j -= 1
                result[0].append(str1[j])
                result[1].append(str2[i])
            elif cost[i][j-1] - penalty == cost[i][j]:
                j -= 1
                result[1].append("-")
                result[0].append(str1[j])
            elif cost[i-1][j] - penalty == cost[i][j]:
                i -= 1
                result[0].append("-")
                result[1].append(str2[i])
        if len(result[0]) > len(max_result):
            max_result = result
    return[max_cost, "".join(reversed(max_result[0])), "".join(reversed(max_result[1]))]


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    print("\n".join(map(str, get_fitting_alighment(str1, str2, 2))), file=file)
