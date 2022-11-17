
#----------------------- Exemple 1 ---------------------#
print("Exemplo 1")
def decorated(decorator):  
    print("decorated recebeu ", end='')
    decorator()

@decorated
def decorator():
    print("decorator")
decorator
#-------------------------------------------------------#

#----------------------- Exemple 2 ---------------------#
print("Exemplo 2")
def decorated(decorator):  
    print("decorated recebeu ", end='')
    decorator()

def decorator():
    print("decorator")

call_decorator=decorated(decorator)
call_decorator
#-------------------------------------------------------#

#----------------------- Exemple 3 ---------------------#
print("Exemplo 3")
def decorated(decorator):
    def internal_decorated(*args):
        print("decorated recebeu ", end='')
        return decorator(*args)
    return internal_decorated

@decorated
def decorator(*args):
    print("decorator")
    print("decorator recebeu",end=" ")
    print(*args, sep=",")
decorator(4,5,6)
#-------------------------------------------------------#

#----------------------- Exemple 4 ---------------------#
print("Exemplo 4")
def decorated(decorator):
    def internal_decorated(*args):
        print("decorated recebeu ", end='')
        return decorator(*args)
    return internal_decorated

def decorator(*args):
    print("decorator")
    print("decorator recebeu",end=" ")
    print(*args, sep=",")

call_decorator=decorated(decorator)
call_decorator(4,5,6)
#-------------------------------------------------------#

