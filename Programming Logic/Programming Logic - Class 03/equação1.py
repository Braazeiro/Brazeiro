'''
Este programa encontra a raiz real de uma equação de primeiro grau.
Termo geral:

    ax + b = 0

Autor: Júlio Cesar Gavilan
Data: 28/09/2022
'''

a = float(input("Type 'a', the value dependent of x "))

if (a == 0):
    print("não tem solução")
else:
    b = float(input("Digite o valor do termo independente ...b"))
    x = -b/a
    print("o valor da raiz x =",x)
#fim se

print ("FIM DO PROGRAMA")