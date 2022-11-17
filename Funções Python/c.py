palavra = "ovo"
produtos = ["arroz", "feijao"]
codigo = ["",""]


igual = []
x = ""
alfabeto = ['a','b',"c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q', 'r','s','t','u','v','x','w','y','z']

for i in range(len(palavra)):
    print(palavra[i])
    for j in range(len(alfabeto)):
        print(" ",alfabeto[j])
        if palavra[i] == alfabeto[j]:
            j=str(j)
            x = x + j

igual.append(x)
print(igual)


for i in range(len(produtos)):
    print(produtos[i])   
        
print("------------------------------")


for i, produto in enumerate(produtos, start="igual"):
    print(i, produto)





print("------------------------------")


print("------------------------------")


