# Find a Cyclic Peptide with Theoretical Spectrum Matching an Ideal Spectrum
# https://rosalind.info/problems/ba4e/

# from copy import deepcopy
# from itertools import combinations
from utilities import get_file, get_answer_file

def cyclopeptide_sequencing(spectrum):
	weights = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
	result = set()
	peptides = [[]]

	def cyclospectrum_peptide(peptide):
		spec = [0, sum(peptide)]
		tmp = peptide + peptide
		for k in range(1, len(peptide)):
			for i in range(len(peptide)):
				spec.append(sum(tmp[i:i+k]))
		spec.sort()
		return spec

	
	def linear_spectrum(peptide):
		prefix_weight = [0]
		for i in range(len(peptide)):
			prefix_weight.append(peptide[i] + prefix_weight[i])
		linear_spec = [0]
		for i in range(len(peptide)):
			for j in range(i+1, len(peptide)+1):
				linear_spec.append(prefix_weight[j]-prefix_weight[i])
		linear_spec.sort()
		return linear_spec

	def expand():
		new_peptides = []
		for pep in peptides:
			for weight in weights:
				new_peptides.append(pep + [weight])
		return new_peptides
	
	def consistent(peptide):
		if sum(peptide) > spectrum[-1] - weights[0]:
			return False
		linear_spec = linear_spectrum(peptide)
		for weight in linear_spec:
			if weight not in spectrum:
				return False
		return True
	
	while peptides:
		peptides = expand()
		for peptide in peptides:
			if sum(peptide) == spectrum[-1]:
				if cyclospectrum_peptide(peptide) == spectrum:
					result.add("-".join(map(str, peptide)))
				peptides = [pep for pep in peptides if pep != peptide]
			elif not consistent(peptide):
				peptides = [pep for pep in peptides if pep != peptide]
	result = list(result)
	return sorted(result)[::-1]
	


with get_file() as file:
	spectrum = list(map(int, file.readline().split()))

with get_answer_file() as file:
    print(" ".join(cyclopeptide_sequencing(spectrum)), file=file)