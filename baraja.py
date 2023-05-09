import streamlit as st
import requests
baraja=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
baraja_id=


st.header("Baraja, cartas al azar")


if(st.button("Carta al azar")):
    st.markdown(":red[lo estás haciendo muy bien]")


https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2

