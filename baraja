import random
palos="Copas Espadas Bastos Oros"
numeros="1 2 3 4 5 6 7 Sota Caballo Rey"
palito=palos.split(" ")
numerito=numeros.split(" ")
palos_lis=[]
#print(palito)
#print(numerito)
for p in palito:
  for n in numerito: 
    palos_lis.append(n+p)
print(palos_lis)
total=len(palos_lis)
print(total)
x=input("¿Cuántas cartas quieres?:")
z=int(x)
cartas=[]
while z!=0:
  c=random.choice(palos_lis)
  cartas.append(c)
  palos_lis.remove(c)
  z-=1
print(cartas)
