# Transcribing DNA into RNA
# http://rosalind.info/problems/rna/

from utilities import get_file, convert_DNA_to_RNA

with get_file() as file:
    strand = file.readline().rstrip()

print(convert_DNA_to_RNA(strand))