# Compute the Probability of a String Emitted by an HMM
# http://rosalind.info/problems/ba10d/

from utilities import get_file, read_dic, read_transition_mat, read_emission_mat, get_answer_file

def get_property_mat(x, sigma, states, transition, emission):
    property_mat = [[0] * len(x) for _ in range(len(states))]
    for i in range(len(states)):
        property_mat[i][0] = 1.0 / len(states) * emission[i][sigma[x[0]]]

    for i in range(len(x)-1):
        for j in range(len(states)):
            property_mat[j][i+1] = emission[j][sigma[x[i+1]]] * sum(property_mat[k][i] * transition[k][j] for k in range(len(states)))
        
    return property_mat

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
    property_mat = get_property_mat(x, sigma, states, transition, emission)
    print(sum(property_mat[i][-1] for i in range(len(states))), file=file)