# Find a Highest-Scoring Multiple Sequence Alignment
# https://rosalind.info/problems/ba5m/

from utilities import get_file, get_answer_file

def get_multiple_subsequence(str1, str2, str3):
    cost = [[[0]*(len(str1)+1) for _ in range(len(str2)+1)] for _ in range(len(str3)+1)]

    for i in range(1, len(str3)+1):
        for j in range(1, len(str2)+1):
            for k in range(1, len(str1)+1):
                if str3[i-1] == str2[j-1] and str2[j-1] == str1[k-1]:
                    cost[i][j][k] = 1 + cost[i-1][j-1][k-1]
                else:
                    # print(len(cost[0][0]))
                    # print(k, j, i)
                    cost[i][j][k] = max(cost[i-1][j-1][k-1], cost[i-1][j-1][k], cost[i][j-1][k-1], cost[i-1][j][k-1], cost[i-1][j][k], cost[i][j-1][k], cost[i][j][k-1])
    i = len(str3)
    j = len(str2)
    k = len(str1)
    print(cost[-1][-1][-1])
    result = [[], [], []]
    while i != 0 and j != 0 and k != 0:
        print(i, j, k)
        print(cost[i][j][k])
        print(cost[i-1][j-1][k-1], cost[i-1][j-1][k], cost[i][j-1][k-1], cost[i-1][j][k-1], cost[i-1][j][k], cost[i][j-1][k], cost[i][j][k-1])
        if cost[i-1][j-1][k-1] + 1 == cost[i][j][k] and str3[i-1] == str2[j-1] and str2[j-1] == str1[k-1]:
            i -= 1
            j -= 1
            k -= 1
            result[0].append(str1[k])
            result[1].append(str2[j])
            result[2].append(str3[i])
        elif cost[i-1][j-1][k-1] == cost[i][j][k]:
            i -= 1
            j -= 1
            k -= 1
            result[0].append(str1[k])
            result[1].append(str2[j])
            result[2].append(str3[i])
        elif cost[i-1][j-1][k] == cost[i][j][k]:
            i -= 1
            j -= 1
            result[0].append('-')
            result[1].append(str2[j])
            result[2].append(str3[i])
        elif cost[i][j-1][k-1] == cost[i][j][k]:
            j -= 1
            k -= 1
            result[0].append(str1[k])
            result[1].append(str2[j])
            result[2].append('-')
        elif cost[i-1][j][k-1] == cost[i][j][k]:
            i -= 1
            k -= 1
            result[0].append(str1[k])
            result[1].append('-')
            result[2].append(str3[i])
        elif cost[i-1][j][k] == cost[i][j][k]:
            i -= 1
            result[0].append('-')
            result[1].append('-')
            result[2].append(str3[i])
        elif cost[i][j-1][k] == cost[i][j][k]:
            j -= 1
            result[0].append('-')
            result[1].append(str2[j])
            result[2].append('-')
        elif cost[i][j][k-1] == cost[i][j][k]:
            k -= 1
            result[0].append(str1[k])
            result[1].append('-')
            result[2].append('-')
    while i != 0 and j != 0:
        i -= 1
        j -= 1
        result[0].append('-')
        result[1].append(str2[j])
        result[2].append(str3[i])
    while j != 0 and k != 0:
        j -= 1
        k -= 1
        result[0].append(str1[k])
        result[1].append(str2[j])
        result[2].append('-')
    while i != 0 and k != 0:
        i -= 1
        k -= 1
        result[0].append(str1[k])
        result[1].append('-')
        result[2].append(str3[i])
    while i != 0:
        i -= 1
        result[0].append('-')
        result[1].append('-')
        result[2].append(str3[i])
    while j != 0:
        j -= 1
        result[0].append('-')
        result[1].append(str2[j])
        result[2].append('-')
    while k != 0:
        k -= 1
        result[0].append('-')
        result[1].append('-')
        result[2].append(str3[i])
    return[cost[-1][-1][-1], "".join(reversed(result[0])), "".join(reversed(result[1])), "".join(reversed(result[2]))]


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()
    str3 = file.readline().rstrip()

with get_answer_file() as file:
    print("\n".join(map(str, get_multiple_subsequence(str1, str2, str3))), file=file)
