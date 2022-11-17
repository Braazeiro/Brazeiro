'''
This program receives by *args an indefinite amount of numbers and 
to return the four fundamental mathematical operations in the console.

And it receives by **kwargs the names and signs of these operations
to return it in the console.

    n1 + n2 + n3 + n4 + n5... = a
    n1 - n2 - n3 - n4 - n5... = b
    n1 * n2 * n3 * n4 * n5... = c
    n1 / n2 / n3 / n4 / n5... = d

Author: Guilherme Brazeiro Ramos
Data: 2022-11-14

'''

#Função decorada que exibe as informações no console 
def display(operation):
    def result(*args, **kwargs):
        
        print("--------------------------------------------")

        for operat, sign in kwargs.items():
            print(f"\n( {sign} ) is used in the {operat}")
        #end_for#

        for i in range(len(args)):
            if i > 0:
                print(sign, end=" ")
            print(args[i], end=" ")
        #end-for#
             
        print(f" = {operation(*args)}\n")

    return result
#Função decorada que exibe as informações no console 

# |-----------------------------------| #
# |    Four Fundamental Operations    | #
# V-----------------------------------V #

#Addition#
@display
def add(*args):
    sum=0
    for number in args:
        sum+=number
    return sum

#Subtraction#
@display
def subtract(*args):
    difference=args[0]*2
    for number in args:
        difference-=number
    return difference

#Multiplication#
@display
def multiply(*args):
    product=1
    for number in args:
        product*=number
    return product

#Division#
@display
def divide(*args):
    quociente=args[0]**2
    for number in args:
        quociente/=number
    return quociente

# A-----------------------------------A #
# |    Four Fundamental Operations    | #
# |-----------------------------------| # 

#numbers received for *args
numbers = [5,4,3,2,1]

#title#
print()
print("      The four fundamental operations".upper())

#call functions#
add(*numbers,addition = "+")
subtract(*numbers,subtraction = "-")
multiply(*numbers,multiplication = "*")
divide(*numbers,division = "/")











