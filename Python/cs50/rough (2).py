import csv
from sys import argv

def get_max(s,sub):
    ans = [0] * len(s)
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i+len(sub)] == sub:
            if i + len(sub) > len(s) -1:
                ans[i] = 1
            else:
                ans[i] =  1 + ans[i+ len(sub)]
    return max(ans)
def old(s,sub):
    i = 0
    while sub*(i+1) in s:
        i+=1
    return i
        
def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run
"""get_max , old and longest_match all give same output. subsequence repeat in sequence """
def print_match(reader,actual):
    for line in reader:
        person = line[0]
        values = [int(val) for val in line[1:]]
        if values == actual:
            print(person)
            return
    print('No match')

def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)
    with open(argv[1],'r') as f:
        reader = csv.reader(f)
        all_seq = next(reader)[1:]
        with open(argv[2],'r') as f:
            t= f.read()
            actual = [longest_match(t,seq) for seq in all_seq]
        print_match(reader,actual)
    
main()