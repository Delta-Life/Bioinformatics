# Finding a Protein Motif
# http://rosalind.info/problems/mprt/
# This problem has issues related to windows newline charactor.
# You should submit answer as text file.

from utilities import get_file
import urllib.request
import re

def get_name_array(file):
    name_array = []
    for i in file.readlines():
        name_array.append(i.rstrip())
    return name_array

def get_FASTA_on_web(name_array):
    fasta_array = []
    for i in name_array:
        rawFasta = urllib.request.urlopen("https://www.uniprot.org/uniprot/" + i + ".fasta").read()
        fasta_array.append("".join(str(rawFasta).split("\\n")[1:]))
    return fasta_array

def find_glycosylation(fasta_array):
    glycosylation_array = []
    point_array = []
    re_glycosylation = re.compile("(?=N[^P][ST][^P])")
    for n, i in enumerate(fasta_array):
        if re_glycosylation.search(i) != None:
            point_array.append(n)
            glycosylation_array.append([j.start() + 1 for j in re_glycosylation.finditer(i)])

    return point_array, glycosylation_array

with get_file() as file:
    name_array = get_name_array(file)

fasta_array = get_FASTA_on_web(name_array)
point_array, glycosylation_array = find_glycosylation(fasta_array)
for i, j in zip(point_array, glycosylation_array):
    print(name_array[i])
    print(" ".join(map(str, j)))