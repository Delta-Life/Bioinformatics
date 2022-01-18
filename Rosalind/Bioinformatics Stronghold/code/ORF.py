# Open Reading Frames
# http://rosalind.info/problems/orf/

from utilities import get_file, read_FASTA, translate_strand, complemente_strand, DNA_to_RNA
import re

def find_ORF(strand):
    RNA_strand1 = DNA_to_RNA(strand)
    RNA_strand2 = DNA_to_RNA(complemente_strand(strand))
    ORF_array = []
    re_stop = re.compile("(?=%s)" % "Stop")
    re_start = re.compile("(?=%s)" % "M")

    for i in range(0, 3):
        protein_string = translate_strand(RNA_strand1[i:])
        for j in re_stop.finditer(protein_string):
            for k in re_start.finditer(protein_string[:j.start()]):
                if protein_string[k.start():j.start()].find("Stop") == -1:
                    ORF_array.append(protein_string[k.start():j.start()])
    
    for i in range(0, 3):
        protein_string = translate_strand(RNA_strand2[i:])
        for j in re_stop.finditer(protein_string):
            for k in re_start.finditer(protein_string[:j.start()]):
                if protein_string[k.start():j.start()].find("Stop") == -1:
                    ORF_array.append(protein_string[k.start():j.start()])
    
    return list(set(ORF_array))


with get_file() as file:
    _, strand = read_FASTA(file)

for i in find_ORF(strand[0]):
    print(i)