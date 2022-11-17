animais = ["Cachorro","Gato",'Periquito','Elefante']
print(list(enumerate(animais)))
#Iterar um uma lista com enumerate

for i, valor in enumerate(animais):
    print(i,valor)
#Iterador e Enumerate com Condicionais

print()

for i, valor in enumerate(animais):
    if i > 1:
        break
    else:
        print(valor)

print()

for i, valor in enumerate(animais):
    print(animais[i])