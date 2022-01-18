# Finding a Motif in DNA
# http://rosalind.info/problems/subs/

import re
from utilities import get_file

def find_motif(strand, motif):
    re_motif = re.compile('(?=%s)' % motif)
    return [i.start() for i in re_motif.finditer(strand)]

with get_file() as file:
    strand = file.readline().rstrip()
    motif = file.readline().rstrip()

print(" ".join(map(str, find_motif(strand, motif))))