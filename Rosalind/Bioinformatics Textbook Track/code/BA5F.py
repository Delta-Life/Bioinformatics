# Find a Highest-Scoring Local Alignment of Two Strings
# https://rosalind.info/problems/ba5f/

from utilities import get_file, get_answer_file, load_pam250, load_protein_dictionary

def get_local_alignment(str1, str2, score_matrix):
    protein_dict = load_protein_dictionary()
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(cost)):
        cost[i][0] = -5 * i
    for i in range(len(cost[0])):
        cost[0][i] = -5* i
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j]-5, cost[i][j-1]-5, cost[i-1][j-1]+score_matrix[protein_dict[str2[i-1]]][protein_dict[str1[j-1]]], 0)

    max_cost = 0
    for n1, k in enumerate(cost):
        for n2, l in enumerate(k):
            if max_cost < l:
                max_cost = l
                i = n1
                j = n2
    result = [[], []]
    while i * j != 0:
        if cost[i][j-1] - 5 == cost[i][j]:
            j -= 1
            result[1].append("-")
            result[0].append(str1[j])
        elif cost[i-1][j] - 5 == cost[i][j]:
            i -= 1
            result[0].append("-")
            result[1].append(str2[i])
        elif cost[i-1][j-1] == 0:
            result[0].append(str1[j-1])
            result[1].append(str2[i-1])
            i = 0
            j = 0
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
    PAM250 = load_pam250()
    print("\n".join(map(str, get_local_alignment(str1, str2, PAM250))), file=file)
