# Complementing a Strand of DNA
# http://rosalind.info/problems/revc/

from utilities import get_file, get_complement_strand

with get_file() as file:
    strand = file.readline().rstrip()

print(get_complement_strand(strand))