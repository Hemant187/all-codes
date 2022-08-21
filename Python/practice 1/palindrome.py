print("Enter a Number: ")
num = int(input())
temp = num
reverse = 0
'''6574
--> 4 '''

while(num>0):
    dig = num%10
    reverse = reverse *10 +dig
    num = num//10

# num =45
# num = num//10
# print(num) --> it gives 4

if temp == reverse:
    print("This is a palindrome number")
else:
        print("This is not a palindrome number")
print(reverse)
