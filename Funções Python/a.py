import numpy



a=numpy.array([1,2,3])
number=numpy.array([1])
print(a)
print(number[0])

access_number=0

def access_count(decorated_function):
    def nova_func(*args,**kwargs):
        global access_number
        access_number += 1
        return decorated_function(*args,**kwargs)
    return nova_func

def add(*args):
    sum=0
    for i in range(args.len()):
        print(i)
    return sum

def subtract(*args):
    print("Subtract")
    
    for number in (args):
        print(number)


def multiply(*args):
    product=0
    for number in args:
        product*=number
    return product

def divide(*args):
    quotient=args[0]
    for number in args:
        quotient/=number
    return quotient

call=access_count(add)
print(call(2,3))

call=access_count(subtract)
print(call(2,3))

call=access_count(multiply)
print(call(2,3))

call=access_count(divide)
print(call(2,3))