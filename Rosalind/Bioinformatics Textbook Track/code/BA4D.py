# Compute the Number of Peptides of Given Total Mass
# https://rosalind.info/problems/ba4d/

from utilities import get_file, get_answer_file

def get_num_of_peptide(mass):
    weights = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    ways = [0]*(mass + 1)
    index = mass
    ways[mass] = 1
    while index > 0:
        for weight in weights:
            ways[index-weight] += ways[index]
        index -= 1
        while ways[index] == 0:
            index -= 1
    return ways[0]


with get_file() as file:
    mass = int(file.readline().rstrip())

with get_answer_file() as file:
    print(get_num_of_peptide(mass), file=file)