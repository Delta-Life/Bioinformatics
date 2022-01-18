# GenBank Introduction
# https://rosalind.info/problems/gbk/

from Bio import Entrez
from utilities import get_file, get_answer_file

def get_genbank_nucleotide_records(query):
    handle = Entrez.esearch(db='nucleotide', term=query)
    records = Entrez.read(handle)
    return records

Entrez.email = 'iljung0810@gmail.com'

with get_file() as file:
    genus = file.readline().strip()
    startDate = file.readline().strip()
    endDate = file.readline().strip()
    query = '%s[Organism] AND %s:%s[PDAT]' % (genus, startDate, endDate)

    #  Print output
with get_answer_file() as file:
    print(get_genbank_nucleotide_records(query)['Count'], file=file)