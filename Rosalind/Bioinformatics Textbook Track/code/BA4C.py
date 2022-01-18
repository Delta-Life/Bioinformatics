# Generate the Theoretical Spectrum of a Cyclic Peptide
# https://rosalind.info/problems/ba4c/

from itertools import combinations
from utilities import get_file, get_answer_file

def get_amino_acid_mass_dict(): 
    array = ["G 57", "A 71", "S 87", "P 97", "V 99", "T 101", "C 103", "I 113", "L 113", "N 114", "D 115", "K 128", "Q 128", "E 129", "M 131", "H 137", "F 147", "R 156", "Y 163", "W 186"]
    array = [i.split() for i in array]
    return {i:int(j) for i, j in array}

def cyclospectrum(peptide):
    tmp = peptide + peptide
    amino_mass_dict = get_amino_acid_mass_dict()
    cyclospectrum = []
    cyclosubs = ['', peptide]
    for i, j in combinations(range(0, len(peptide)), 2):
        cyclosubs.append(tmp[i:j])
    for i, j in combinations(range(0, len(tmp)), 2):
        if j-i < len(peptide) and j>len(peptide)-1 and len(peptide)>i:
            cyclosubs.append(tmp[i:j])
    for peptide in list(cyclosubs):
        sum = 0
        for amino_acid in peptide:
            sum += amino_mass_dict[amino_acid]
        cyclospectrum.append(sum)

    return sorted(cyclospectrum)

with get_file() as file:
    peptide = file.readline().rstrip()

with get_answer_file() as file:
    print(" ".join(map(str, cyclospectrum(peptide))), file=file)