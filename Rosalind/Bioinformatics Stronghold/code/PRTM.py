# Calculating Protein Mass
# http://rosalind.info/problems/prtm/

from utilities import get_file, read_all

amino_acid_mass_string = """A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333 """.split()

amino_acid_mass_dict = {amino_acid_mass_string[i]:float(amino_acid_mass_string[i+1]) for i in range(0, len(amino_acid_mass_string), 2)}

with get_file() as file:
    protein_string = read_all(file)
total_mass = 0

for amino_acid in protein_string:
    total_mass += amino_acid_mass_dict[amino_acid]

print("%.3f" % total_mass)