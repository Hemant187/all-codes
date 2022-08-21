with open('currency.txt') as f:
    lines = f.readlines()

currencydict = {}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]]=parsed[1]

amount = int(input("Enter amount:\n"))
[print(item) for item in currencydict.keys()]
currency= input("Please enter one of the values: \n")
print(f"{amount} INR is equal to {amount * float(currencydict[currency])} {currency}")