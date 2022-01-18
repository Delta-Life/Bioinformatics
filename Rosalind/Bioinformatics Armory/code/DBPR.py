# Introduction to Protein Databases
# http://rosalind.info/problems/dbpr/

from Bio import ExPASy, SwissProt
from utilities import get_file, get_answer_file

def get_gene_ontology(name):
    handle = ExPASy.get_sprot_raw(name)
    record = SwissProt.read(handle)
    return [line[2][2:] for line in record.cross_references if line[0] == 'GO' and line[2].startswith('P')]

with get_file() as file:
    name = file.readline().rstrip()

with get_answer_file() as file:
    gene_ontology_array = get_gene_ontology(name)
    print('\n'.join(gene_ontology_array), file=file)