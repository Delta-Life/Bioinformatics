# Align Two Strings Using Linear Space
# https://rosalind.info/problems/ba5l/

import sys  
from utilities import get_file, get_answer_file, load_blosum62, load_protein_dictionary

sys.setrecursionlimit(15000)

def get_linear_space_alignment(str1, str2, score_matrix, penalty):
    protein_dict = load_protein_dictionary()

    def get_middle_matrix(top, bottom, left, right, reverse=False):
        cost = [[0]*(bottom-top+1) for _ in range(2)]
        if right - left == 0:
            for i in range(len(cost[0])):
                cost[1][i] = -penalty * i
            return cost
        if bottom-top < 100:
            print(bottom, top)
        for i in range(len(cost)):
            cost[i][0] = -penalty * i
        for i in range(len(cost[0])):
            cost[0][i] = -penalty * i
        if reverse:
            for i in range(1, right-left+1):
                for j in range(1, bottom-top+1):
                    cost[1][j] = max(cost[0][j]-penalty, cost[1][j-1]-penalty, cost[0][j-1]+score_matrix[protein_dict[str1[bottom-j]]][protein_dict[str2[right-i]]])
                if i != right-left:
                    cost.pop(0)
                    cost.append([0]*(bottom-top+1))
                    cost[1][0] = cost[0][0] - penalty
        else:
            for i in range(1, right-left+1):
                for j in range(1, bottom-top+1):
                    cost[1][j] = max(cost[0][j]-penalty, cost[1][j-1]-penalty, cost[0][j-1]+score_matrix[protein_dict[str1[top+j-1]]][protein_dict[str2[left+i-1]]])
                if i != right-left:
                    cost.pop(0)
                    cost.append([0]*(bottom-top+1))
                    cost[1][0] = cost[0][0] - penalty
        return cost

    def get_middle_edge(top, bottom, left, right):
        middle = (left + right)//2+1
        forward_half = get_middle_matrix(top, bottom, left, middle)
        backward_half = get_middle_matrix(top, bottom, middle, right, reverse=True)
        # print(forward_half[1], backward_half[1])
        # print(len(backward_half[0]), bottom-top+1, "!!")
        # print([forward_half[1][i] for i in range(len(backward_half[0]))], [backward_half[1][len(backward_half[0])-1-i] for i in range(len(backward_half[0]))])
        middle_cost = [forward_half[1][i] + backward_half[1][bottom-top-i] for i in range(bottom-top+1)]
        max_cost = max(middle_cost)
        j = middle - left
        i = middle_cost.index(max_cost)
        # print(i, j)
        if forward_half[1][i-1] - penalty == forward_half[1][i]:
            # print(top+i-1, left+j, 2)
            return [top+i-1, left+j, 2]
        elif forward_half[0][i] - penalty == forward_half[1][i]:
            # print(top+i, left+j-1, 0)
            return [top+i, left+j-1, 0]
        else:
            # print(top+i-1, left+j-1, 1)
            return [top+i-1, left+j-1, 1]


    def linear_space_alighment(top, bottom, left, right):
        if left == right:
            return "0" * (bottom - top)
        if top == bottom:
            return "2" * (right - left)
        
        y, x, edge = get_middle_edge(top, bottom, left, right)
        if edge == 2:
            x2 = x + 1
            y2 = y
        if edge == 1:
            x2 = x + 1
            y2 = y + 1
        if edge == 0:
            y2 = y + 1
            x2 = x
        return linear_space_alighment(top, y, left, x) + str(edge) + linear_space_alighment(y2, bottom, x2, right)
    
    path = linear_space_alighment(0, len(str1), 0, len(str2))
    result = [[], []]
    x, y = 0, 0
    cost = 0
    for p in path:
        if p == "0":
            cost -= penalty
            result[0].append(str1[y])
            result[1].append("-")
            y += 1
        elif p == "1":
            result[0].append(str1[y])
            result[1].append(str2[x])
            cost += score_matrix[protein_dict[str1[y]]][protein_dict[str2[x]]]
            x +=1
            y +=1
        elif p == "2":
            result[0].append("-")
            result[1].append(str2[x])
            cost -= penalty
            x +=1

    return [str(cost), "".join(result[0]), "".join(result[1])]

with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    print("\n".join(get_linear_space_alignment(str1, str2, load_blosum62(), 5)), file=file)
