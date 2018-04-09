def superposicion(a,b):
    for c in a:
        if c in b:
            return True
    return False


algunas_frutas = ["manzana", "pera", "durazno" ]
otras_frutas = ["limon", "kiwi", "durazno", "banana" ]

print(superposicion(algunas_frutas,otras_frutas))
