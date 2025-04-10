import streamlit as st
from random import randint

st.title("Simulering av myntkast")

# Brukerinput
antallkast = st.number_input("Kor mange gonger skal vi kaste mynten?", min_value=1, value=10, step=1)
antallrunder = st.number_input(f"...og kor mange simuleringar skal vi gjera av desse {antallkast} kasta?", min_value=1, step=1)

lengde=st.number_input("Kor langt mønster skal vi undersøke? ", max_value=antallkast, value=4)
# Kjør simulering når brukeren trykker på knappen
if st.button("Køyr simulering"):
    hhhh = 0
    hhht = 0
    begge = 0
    ingen = 0

    st.write("### Resultat frå kvar simulering:")
    st.write("Vi ser etter sekvensene "+ lengde*" **:red[K]**" + " og " + (lengde-1)* " **:red[K]**"+" **:blue[M]**")
    
    for k in range(antallrunder):
        resultat = ""
        for i in range(antallkast):
            penge = randint(1, 2)
            resultat += " **:red[K]**" if penge == 1 else " **:blue[M]**"

        st.write(resultat)
        
        
        # Sjekk mønstre
        #inneholder_hhhh = " :red[H] :red[H] :red[H] :red[H]" in resultat
        #inneholder_hhht = " :red[H] :red[H] :red[H] :blue[T]" in resultat
        

        inneholder_hhhh = lengde* " **:red[K]**" in resultat
        inneholder_hhht = (lengde-1)* " **:red[K]**" +" **:blue[M]**" in resultat

        if inneholder_hhhh and not inneholder_hhht:
            hhhh += 1
            st.write("→ "+lengde*" **:red[K]**")
        elif inneholder_hhht and not inneholder_hhhh:
            hhht += 1
            st.write("→ "+(lengde-1)*" **:red[K]**"+" **:blue[M]**")
        elif inneholder_hhhh and inneholder_hhht:
            begge += 1
            st.write("→ Begge mønstra")
        else:
            ingen += 1
            st.write("→ Ingen av mønstra")

    st.write("---")
    st.write("## Oppsummering:")
    st.write(f"Begge mønstra: {begge}")
    st.write(f"Berre "+lengde*" **:red[K]**"+f": {hhhh}")
    st.write(f"Berre "+(lengde-1)*" **:red[K]**"+" **:blue[M]**"+f": {hhht}")
    st.write(f"Ingen av mønstra: {ingen}")
