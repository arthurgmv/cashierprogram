Total = 0

while True:
    product = str(input("Product name: "))
    price = float(input("Cost: "))
    Total += price
    if price > 1000:
        tothousand =+ 1 
    resp = ' '
    while resp not in 'YN':
        resp = str(input("Anything else? [Y/N] ")).strip().upper()[0]
    if resp == 'N':
        break
print ('{:-^40}'.format(" END "))
print (f"The total ammount to pay is: USD {price:10.2f}")
print (f"There is/are {tothousand} product(s) costing more than USD 1000,00")
