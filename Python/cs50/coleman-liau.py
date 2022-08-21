# Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8,
#  where L is the average number of letters per 100 words in the text, and
#  S is the average number of sentences per 100 words in the text.
# Use get_string from the CS50 Library to get the user’s input, and print to output your answer.
# Your program should count the number of letters, words, and sentences in the text. 
# You may assume that a letter is any lowercase character from a to z or any uppercase character 
# from A to Z, any sequence of characters separated by spaces should count as a word, and that 
# any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
# Your program should print as output "Grade X" where X is the grade level computed by the Coleman-Liau formula,
#  rounded to the nearest integer.
# If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level)
# , your program should output "Grade 16+" instead of giving the exact index number. 
# If the index number is less than 1, your program should output "Before Grade 1".
from cs50 import get_string
text = get_string("Text: ")
space = text.count(" ")
#count the number of letters
letters =0
sentences =0
for i in range(len(text)):
    if text[i].isalpha():
        letters +=1
    if text[i]=='?' or text[i]=='.' or text[i]=='!':
        sentences+=1
words = len(text.split())
L = letters/words*100
S = sentences/words*100
index= round(0.0588 * L - 0.296 * S - 15.8)
if index<1:
    print("Before Grade 1")
if index>=16:
    print("Grade 16+")
else:
    print(f"Grade {index}")



