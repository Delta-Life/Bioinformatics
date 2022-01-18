# Find the Reverse Complement of a String
# https://rosalind.info/problems/ba1c/

from utilities import get_file, get_answer_file

def get_complement_strand(strand):
    translator = str.maketrans("ATGC", "TACG")
    return strand[::-1].translate(translator)

with get_file() as file:
    strand = file.readline().rstrip()

with get_answer_file() as file:
    print(get_complement_strand(strand), file=file)