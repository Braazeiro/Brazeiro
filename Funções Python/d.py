numbers = [68,902,5,35,90]

parOuImpar = list(range(len(numbers)))

for i, number in enumerate(numbers):

    if number % 2 == 0:
        parOuImpar[i] = "Even"      
    else:
        parOuImpar[i] = "Odd"

    print(f"Index: {i} \nValue: {number} \nEven or Odd? {parOuImpar[i]}\n")



