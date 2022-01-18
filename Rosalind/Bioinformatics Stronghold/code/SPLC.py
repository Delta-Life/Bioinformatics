# RNA Splicing
# http://rosalind.info/problems/splc/

from utilities import get_file, read_FASTA, convert_DNA_to_RNA, translate_strand, get_complement_strand

def get_exon(strand_array):
    exon =  strand_array[0]
    for j in strand_array[1:]:
        exon = exon.replace(j, "")

    return translate_strand(convert_DNA_to_RNA(exon)).split("Stop")
with get_file() as file:
    _, strand_array = read_FASTA(file)

print(get_exon(strand_array)[0])