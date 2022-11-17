# O parâmetro args é utilizado quando não sabemos quantos argumentos a função receberá.
# O retorno ou saída dessa função retorna uma tupla.

def numbers(*args):
    
    args=list(args)
    args[0]=0
    print(args)

numbers(5,673,34,78,100,32,205,45,90)

def sum(*args):
    total=0
    for n in args:
        total+=n
    return total

print(sum(1,2,3,4,5,6,7,8,9))