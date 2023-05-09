import streamlit as st
st.header("La vida en el mar")
listilla=["sardina","mero","tiburón ballena","pulpo"]
fotillos=["F1","F2","F3"]
elec_animal=st.radio("Elige el animal que más te gusta:",listilla)
if elec_animal==listilla[0]:
    st.error("por el monte la sardina")
elif elec_animal==listilla[1]:
    st.warning("uno mero dos de febrero")
elif elec_animal==listilla[2]:
    st.success("por fin llegamos a lo que interesa")
    st.image("https://www.bekaretransfers.com/blog/wp-content/uploads/2017/05/whaleshark.jpeg")
elif elec_animal==listilla[3]:
    st.text("elige tiburón ballena por favor")
if(st.button("Click me for no reason")):
    st.markdown(":red[lo estás haciendo muy bien]")
elec_foto=st.selectbox("Ahora lo complicado:",
                     ["Elige una foto"]+fotillos)
if elec_foto=="F1":
    st.image("F1.jpg",width=500)
elif elec_foto=="F2":
    st.image("F2.jpg",width=500)
elif elec_foto=="F3":
    st.image("F3.jpg")
