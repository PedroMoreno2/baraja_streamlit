import streamlit as st
import random
palos="Copas Espadas Bastos Oros"
numeros="1 2 3 4 5 6 7 Sota Caballo Rey"
palito=palos.split(" ")
numerito=numeros.split(" ")
palos_lis=[]
for p in palito:
  for n in numerito: 
    palos_lis.append(n+" "+p)
st.write("Hay un total de ",len(palos_lis),"cartas, de los palos "+palos)
x=st.text_input("¿Cuántas cartas quieres?:")
if(st.button("Las quiero YA")):
  z=int(x.title()) 
  cartas=[]
  while z!=0:
    c=random.choice(palos_lis)
    cartas.append(c)
    palos_lis.remove(c)
    z-=1
st.write(cartas)


