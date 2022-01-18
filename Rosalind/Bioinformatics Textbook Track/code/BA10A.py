# Compute the Probability of a Hidden Path
# http://rosalind.info/problems/ba10a/

from utilities import get_file, get_answer_file

def read_dic(file):
    return dict((state, i) for i, state in enumerate(file.readline().split()))

def read_mat(file):
    states = file.readline().split()
    return [list(map(float, i.split()[1:])) for i in file.readlines()]

def get_property(pi, states, transition):
    property = 0.5
    for i, j in zip(pi[:-1], pi[1:]):
        property *= transition[states[i]][states[j]]
    
    return property


with get_file() as file:
    pi = file.readline().rstrip()
    file.readline()
    states = read_dic(file)
    file.readline()
    transition = read_mat(file)

with get_answer_file() as file:
    property = get_property(pi, states, transition)
    print('%.12g' %property, file=file)