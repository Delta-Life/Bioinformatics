'''
codes of common fuctions

list:
argmax
comb
convert_DNA_to_RNA
factor
get_codon_table
get_complement_strand
get_file
read_all
read_FASTA
translate_strand
'''

import sys

def bins(target, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid + 1
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search(target, data):
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) // 2
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def get_answer_file():
    filePath = sys.argv[0].split("\\")
    return open("/".join(filePath[:-1]) + "/../answer/rosalind_" + filePath[-1].split(".")[0].lower() + ".txt", 'w')

def get_file():
    filePath = sys.argv[0].split("\\")
    return open("/".join(filePath[:-1]) + "/../data/rosalind_" + filePath[-1].split(".")[0].lower() + ".txt", 'r')

def read_all(file):
    return "".join(line.rstrip() for line in file.readlines())