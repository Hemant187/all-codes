with open("currency.txt") as f:
    lines = f.readlines()
currencydict ={}
for line in lines:
    pardon = line.split('\t')
    currencydict[pardon[0]] =pardon[1]
amount =int(input('enter the money\n'))
[print(item) for item in currencydict.keys()]
currency = input("Converte INK in:\n ")
print(f"{amount} INK is equal to {amount*float(currencydict[currency])} {currency}")