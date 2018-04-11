def mas_larga(l1,l2):
    if( len(l1)>len(l2) ):
        return l1
    else:
        return l2


frutas = ["manzana", "pera", "durazno", "limón"]
frutas2 = ["manzana", "pera", "durazno", "limón","kiwi"]
print(mas_larga(frutas,frutas2))
