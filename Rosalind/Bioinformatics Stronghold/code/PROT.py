# Translating RNA into Protein
# http://rosalind.info/problems/prot/

from utilities import get_file, read_all, translate_strand

with get_file() as file:
    strand = read_all(file)

protein_string = translate_strand(strand).split("Stop")[0]
print(protein_string)