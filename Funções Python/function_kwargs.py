#O parâmetro kwargs deve conter, além do valor, uma chave.

def saudacoes(**kwargs):
    print(kwargs)

saudacoes(manha="bom dia", tarde="boa tarde")

def saudacao_dia(**kwargs):
    for periodo_dia, saudacao in kwargs.items():
        print(f"Durante a {periodo_dia} dizemos {saudacao}") #fstrings
    
    valor = [*kwargs.values()]
    print(list(enumerate(valor)))
    #Iterar um uma lista com enumerate



    print(valor[0])


saudacao_dia(manha="bom dia", tarde="boa tarde",noite="boa noite",madrugada="boa noite" )
           
