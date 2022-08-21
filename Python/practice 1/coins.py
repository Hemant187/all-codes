from cs50 import get_float
# Assumre that the only coins available are 
# quartes (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)
def fun():
    pen =get_float("Enter your $: ")
    if pen>0:
        return act(pen)
    else:
        fun()
def act(pen):
    quarter=pen//.2499999999
    # print('Quarter: ',quarter)
    rem = pen%.2499999999
    # print(rem)
    dimes=rem//.099999999
    # print('Dimes: ',dimes)
    rem1 =rem%.099999999
    # print(rem1)
    nickels =rem1//.0499999999
    # print('Nickels: ',nickels)
    rem2=rem1%0.0499999999
    # print(rem2)
    pennies=rem2//0.00999999999
    # print('Pennies: ',pennies)
    result =quarter+dimes+nickels+pennies
    print("Result: ",result)

fun()