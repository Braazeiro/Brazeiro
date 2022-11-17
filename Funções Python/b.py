from functools import reduce

funlmb = lambda *args : sum(args)
print(funlmb(1,2,3,4,5))

lista = [2022, 1998]
print(lista, type(lista))

#----------------------------------------#

idade = lambda x , y : x - y

q = reduce(idade, lista)



print(q)

data_nascimento = []
i=-1
while (i < 2):
    i=i+1
    data_nascimento.append(input())
    print(data_nascimento[i])
print(data_nascimento)


if len(lista) == 3:
    print(lista)
print(list(enumerate(lista)))

print("[", end="")
for i in range(len(lista)):
    print("(",end="")
    print(i,lista[i], sep=", ",end="")
    print(")",end="")
    if i < len(lista)-1:
        print(", ",end="")
print("]")

#----------------------------------------#

tupla = ("+","-","*","/")
print(tupla, type(tupla))

dicionario = {"+" : "addict", "-" : "subtract", "*" : "multiply", "/" : "divide"}
print(dicionario, type(dicionario))