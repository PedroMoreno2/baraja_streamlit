import streamlit as st
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
st.write(palos_lis)
total=len(palos_lis)
st.write(total)
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


