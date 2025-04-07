import streamlit as st
from random import randint

st.title("Simulering av myntkast")

# Brukerinput
antallkast = st.number_input("Kor mange kast skal vi ha?", min_value=1, value=5, step=1)
antallrunder = st.number_input(f"...og kor mange simuleringar skal vi gjera av desse {antallkast} kasta?", min_value=1, value=5, step=1)

# Kjør simulering når brukeren trykker på knappen
if st.button("Køyr simulering"):
    hhhh = 0
    hhht = 0
    begge = 0
    ingen = 0

    st.write("### Resultat frå kvar simulering:")
    for k in range(antallrunder):
        resultat = ""
        for i in range(antallkast):
            penge = randint(1, 2)
            resultat += " :red[H]" if penge == 1 else " :blue[T]"

        st.write(resultat)

        # Sjekk mønstre
        inneholder_hhhh = " :red[H] :red[H] :red[H] :red[H]" in resultat
        inneholder_hhht = " :red[H] :red[H] :red[H] :blue[T]" in resultat

        if inneholder_hhhh and not inneholder_hhht:
            hhhh += 1
            st.write("→ HHHH")
        elif inneholder_hhht and not inneholder_hhhh:
            hhht += 1
            st.write("→ HHHT")
        elif inneholder_hhhh and inneholder_hhht:
            begge += 1
            st.write("→ Begge mønstra")
        else:
            ingen += 1
            st.write("→ Ingen av mønstra")

    st.write("---")
    st.write("## Oppsummering:")
    st.write(f"Begge mønstra: {begge}")
    st.write(f"Bare HHHH: {hhhh}")
    st.write(f"Bare HHHT: {hhht}")
    st.write(f"Ingen av mønstra: {ingen}")
