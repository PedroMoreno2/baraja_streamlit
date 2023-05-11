import streamlit as st
import requests
baraja=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
codigo=baraja.json()["deck_id"]
# Ahora a sacar una carta de esa baraja:
cartas=requests.get("https://deckofcardsapi.com/api/deck/"+codigo+"/draw/?count=1")
carta_d=cartas.json()["cards"]
carta_image=carta_d[0]["image"]
st.header("Baraja, cartas al azar")
if(st.button("Carta al azar")):
    st.image("carta_image")
