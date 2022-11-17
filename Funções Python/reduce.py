from functools import reduce

lista = [2,7,10,3,78]
def mult(x,y):
    return x * y
print(reduce(mult,lista))

lista2 = [45,1,56,12,6]
testmaior = lambda x,y: x if (x > y) else y
print(reduce(testmaior,lista2))

players = ["player1", "player2", "player3"]

score = [1005, 789, 890]

print(list(enumerate(players)))

