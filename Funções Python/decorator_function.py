#Decorator Function:
#changes the functionality of a function or method at runtime.
#We can decorate a function with variable or decorator.
def function_1(receive_function_2):
    def display():
        print("function 1")
        receive_function_2()
    return display

#Variable
def function_2():
    print("function 2\n")

call_function = function_1(function_2)
call_function()

#Decorator
@function_1
def function_2():
    print("function 2\n")

function_2()

#-------------------------------------#
def decorator(value):
    def display(*args):
        print("Multiply")
        return value(*args)
    return display

@decorator
def multiply(a,b):
    return f"{a} * {b} = {a*b}"

print(multiply(2,3))

def decorator(value):
    def display(*args):
        print("Multiply")
        return value(*args)
    return display

@decorator
def sum(*args):
    mult=1
    for n in args:
        mult*=n
    return mult

print(sum(2,3,6,2,9))

contador = 0

def contar_acessos(funcao_decorada):
    def nova_func(*args, **kwargs):
        global contador
        contador += 1
        return funcao_decorada(*args, **kwargs)
    return nova_func

def sum(*args):
    t=0
    for n in args:
        t+=n
    return t

qwe=contar_acessos(sum)
qwe(2,7)
print("asasa",qwe(2,3))

print(contador)
print(sum(2,2,6))
print(contador)

print(sum(2,2,6))
print(contador)




