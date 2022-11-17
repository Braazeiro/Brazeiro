faturamento = 30000
print("Faturamento =",faturamento)

dicionario = {"Comissao Caixa" : "Cmi Caixa", "Comissao Cozinha" : "4%", "Comissao Gerente" : "6%"}

comissao_caixa = faturamento * 2 / 100
print(dicionario["CC"])

comissao_cozinha = faturamento * 4 / 100
print("Comissao Cozinha =",comissao_cozinha)

comissao_gerente = faturamento * 6 / 100
print("Comissao Gerente =",comissao_gerente)