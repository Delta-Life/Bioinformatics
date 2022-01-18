# Counting Phylogenetic Ancestors
# http://rosalind.info/problems/inod/

from utilities import get_file, get_answer_file

with get_file() as file:
    num = int(file.readline().rstrip())

with get_answer_file() as file:
    print(num-2, file=file)