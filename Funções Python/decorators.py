def name(name):
    print("Nome: " + name.upper())

name("Guilherme")

def uppercase(receive_insert_name):
    def display(*args):
        receive_insert_name(args[0].upper(),args[1].upper())    
    return display
        

@uppercase
def insert_name(name, sobrenome):
    print("Nome: " + name + "\nSobrenome: " + sobrenome)

insert_name("Guilherme", "Brazeiro Ramos")