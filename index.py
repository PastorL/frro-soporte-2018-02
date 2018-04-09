#import math
#n = math.sin( 0.15 )
#print(n)

#c = "La pelota roja"
#print(c[:4])
#print(c[:-2])
#print(c[2:5])

frutas = ["manzana", "pera", "durazno", "limón"]

frutas [:2]
frutas [-1]
frutas [2:3]
frutas.insert(3, "naranja") # -- intercala
del frutas[2] # -- borra
frutas.remove("pera") # -- borra
frutas[1] = "uva"

articulos={ "copa":200, "vaso":120, "tenedor":30}
print(articulos)
