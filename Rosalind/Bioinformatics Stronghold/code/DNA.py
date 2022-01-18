# Counting DNA Nucleotides
# http://rosalind.info/problems/dna/

from utilities import get_file, get_answer_file
from collections import Counter

with get_file() as file:
    strand = file.readline().rstrip()
    counts = Counter(strand)

with get_answer_file() as file:
    print(counts['A'], counts['C'], counts['G'], counts['T'], file=file)