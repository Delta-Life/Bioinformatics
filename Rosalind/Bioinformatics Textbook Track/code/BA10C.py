# Implement the Viterbi Algorithm
# http://rosalind.info/problems/ba10c/

from utilities import get_file, read_dic, read_transition_mat, read_emission_mat, get_answer_file

def backtrack(viterbi_mat, backtrack_mat, states):
    result = []
    un_states = dict((value, key) for key, value in states.items())

    state_index = max(range(len(states)), key=lambda l: viterbi_mat[l][-1])
    for i in range(len(viterbi_mat[0])-1, -1, -1):
        result.append(un_states[state_index])
        state_index = backtrack_mat[state_index][i]
    
    return result[::-1]

def decode(x, sigma, states, transition, emission):
    viterbi_mat = [[0] * len(x) for _ in range(len(states))]
    backtrack_mat = [[0] * len(x) for _ in range(len(states))]

    for i in range(len(states)):
        viterbi_mat[i][0] = 1.0 / len(states) * emission[i][sigma[x[0]]]

    for i in range(len(x)-1):
        for k in range(len(states)):
            viterbi_mat[k][i+1] = emission[k][sigma[x[i+1]]] * max(viterbi_mat[l][i] * transition[l][k] for l in range(len(states)))
            backtrack_mat[k][i+1] = max(range(len(states)), key=lambda l: viterbi_mat[l][i] * transition[l][k])
        
    return backtrack(viterbi_mat, backtrack_mat, states)

with get_file() as file:
    x = file.readline().rstrip()
    file.readline()
    sigma = read_dic(file)
    file.readline()
    states = read_dic(file)
    file.readline()
    transition = read_transition_mat(file)
    file.readline()
    emission =  read_emission_mat(file)

with get_answer_file() as file:
    max_path = decode(x, sigma, states, transition, emission)
    print("".join(max_path), file=file)