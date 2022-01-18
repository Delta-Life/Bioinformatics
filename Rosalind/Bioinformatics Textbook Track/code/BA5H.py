# Find a Highest-Scoring Fitting Alignment of Two Strings
# https://rosalind.info/problems/ba5h/

from utilities import get_file, get_answer_file

def get_fitting_alighment(str1, str2, penalty):
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    match_table = [[-1]*(len(str1)) for _ in range(len(str2))]
    for i in range(len(cost)):
        cost[i][0] = -penalty * i
    for i in range(len(match_table)):
        for j in range(len(match_table[0])):
            if str1[j] == str2[i]:
                match_table[i][j] = 1
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j]-penalty, cost[i][j-1]-penalty, cost[i-1][j-1]+match_table[i-1][j-1])
    i = len(str2)
    result = [[], []]
    max_cost = max(cost[-1])
    j =  cost[-1].index(max_cost)
    while i != 0:
        if cost[i][j-1] - penalty == cost[i][j]:
            j -= 1
            result[1].append("-")
            result[0].append(str1[j])
        elif cost[i-1][j] - penalty == cost[i][j]:
            i -= 1
            result[0].append("-")
            result[1].append(str2[i])
        else:
            j -= 1
            i -= 1
            result[0].append(str1[j])
            result[1].append(str2[i])
    return[max_cost, "".join(reversed(result[0])), "".join(reversed(result[1]))]


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    print("\n".join(map(str, get_fitting_alighment(str1, str2, 1))), file=file)
