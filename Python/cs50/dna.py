import csv
from sys import argv, exit


def longest_match(sequence, subsequence):
    i = 0
    while subsequence*(i+1) in sequence:
        i += 1
    return i


def print_result(reader, actual):
    for line in reader:
        name = line[0]
        value = [int(val) for val in line[1:]]
        if value == actual:
            print(name)
            return
    print("No match")


def main():

    # Check for command-line usage
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Read database file into a variable
    _csv_ = argv[1]
    with open(_csv_) as csv_file:
        reader = csv.reader(csv_file)

        # store all csvfile sequences in a variable
        all_seq = next(reader)[1:]

    # Read DNA sequence file into a variable
        _text_ = argv[2]
        with open(_text_) as text_file:
            dna = text_file.read()
            #  Find longest match of each STR in DNA sequence
            actual = [longest_match(dna, seq) for seq in all_seq]
        #  Check database for matching profiles
        print_result(reader, actual)



main()
