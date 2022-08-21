
# num = int(input("Enter a number: \n"))
# factorial =1
# if num == 0:
#     print(1)
# elif num <0:
#     print("Error! factorial of negative number is not defined ")
# else:
#     for i in range(1,num+1):
#         factorial = factorial*i

#     print(f"Factorial of {num} is {factorial}")
#     # print(f"{num}! = {factorial}")




def factorial(self):
    
    factorial =1
    if self == 0:
        return "Factorial of 0 is 1"
    elif self < 0:
        return "Error! factorial of negative number is not defined "
    else:
        for i in range(1,self+1):
            factorial = factorial*i

        return f"Factorial of {self} is {factorial}"


num =int(input("Enter a number: \n"))
num= factorial(num)
print(num)
a= input()


