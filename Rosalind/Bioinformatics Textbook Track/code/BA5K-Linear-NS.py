# Find a Middle Edge in an Alignment Graph in Linear Space
# https://rosalind.info/problems/ba5k/

from utilities import get_file, get_answer_file, load_blosum62, load_protein_dictionary

def get_half_matrix(score_matrix, str1, str2, penalty):
    protein_dict = load_protein_dictionary()
    cost = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
    for i in range(len(cost)):
        cost[i][0] = -penalty * i
    for i in range(len(cost[0])):
        cost[0][i] = -penalty * i
    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            cost[i][j] = max(cost[i-1][j]-penalty, cost[i][j-1]-penalty, cost[i-1][j-1]+score_matrix[protein_dict[str2[i-1]]][protein_dict[str1[j-1]]])
    
    return cost

def get_middle_edge(str1, str2, score_matrix, penalty):
    protein_dict = load_protein_dictionary()
    def get_middle_matrix(top, bottom, left, right, reverse=False):
        cost = [[0]*(bottom-top+1) for _ in range(2)]
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
    
    middle = (len(str2))//2+1
    # forward_half2 = get_half_matrix(score_matrix, str2[:middle], str1, penalty)
    forward_half = get_middle_matrix(0, len(str1), 0, middle)
    # backward_half2 = get_half_matrix(score_matrix, str2[middle:][::-1], str1[::-1], penalty)
    backward_half = get_middle_matrix(0, len(str1), middle, len(str2), reverse=True)
    print(forward_half[0], backward_half[0])
    # print([forward_half2[i][-2] for i in range(len(forward_half2))], [backward_half2[len(backward_half2)-1-i][-2] for i in range(len(backward_half2))])
    middle_cost = [forward_half[1][i] + backward_half[1][len(str1)-i] for i in range(len(str1))]
    print(middle_cost)
    max_cost = max(middle_cost)
    print(max_cost)
    i = middle
    j = middle_cost.index(max_cost)
    print(i, j)
    result = [[j, i]]

    if forward_half[1][j-1] - penalty == forward_half[1][j]:
        result.insert(0, [j-1, i])
    elif forward_half[0][j] - penalty == forward_half[1][j]:
        result.insert(0, [j, i-1])
    else:
        result.insert(0, [j-1, i-1])

    return result


with get_file() as file:
    str1 = file.readline().rstrip()
    str2 = file.readline().rstrip()

with get_answer_file() as file:
    BLOSUM62 = load_blosum62()
    for i in get_middle_edge(str1, str2, BLOSUM62, 5):
        print(tuple(i), end=' ', file=file)
