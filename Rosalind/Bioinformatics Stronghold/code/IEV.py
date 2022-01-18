# Calculating Expected Offspring
# http://rosalind.info/problems/iev/

from utilities import get_file, get_answer_file

get_offspring = lambda couple: sum(c * w for c, w in zip(couple, [2, 2, 2, 1.5, 1, 0]))

with get_file() as file:
    couple = list(map(int, file.readline().split()))

with get_answer_file() as file:
    print(get_offspring(couple), file=file)