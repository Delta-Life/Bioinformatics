# Generate the Theoretical Spectrum of a Cyclic Peptide
# https://rosalind.info/problems/ba4c/

from utilities import get_file, get_answer_file, cyclospectrum

def get_spectrum_score(peptide, spectrum):
    spectrum_of_peptide = cyclospectrum(peptide)
    score = 0

    for weight in spectrum:
        if weight in spectrum_of_peptide:
            spectrum_of_peptide.pop(spectrum_of_peptide.index(weight))
            score += 1
    
    return score


with get_file() as file:
    peptide = file.readline().rstrip()
    spectrum = list(map(int, file.readline().split()))

with get_answer_file() as file:
    print(get_spectrum_score(peptide, spectrum), file=file)