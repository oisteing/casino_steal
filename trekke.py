import streamlit as st
from random import randint, random

st.title("Trekke brikker ⚫⚪")

st.write("Du har ein pose med svarte og kvite brikker. Du får trekkje ein og så leggje den tilbake.")

# Brukar vel kor mange brikker og utdrag
n = st.number_input("Kor mange brikker er det i posen?", min_value=1, step=1, value=10, key="n_brikkar")
u = st.number_input("Kor mange gonger vil du trekkje ein brikke (altså med tilbakelegging)?", min_value=1, , value=5, step=1, key="u_utdrag")

# Knapp 1: Kjør simulering
if st.button("Køyr simulering"):
    h = randint(0, n)  # kvite brikker
    s = n - h          # svarte brikker
    mulig_svart = s / n

    s_utdrag = 0
    h_utdrag = 0
    resultat = []

    for _ in range(u):
        tilf = random()
        if tilf < mulig_svart:
            s_utdrag += 1
            resultat.append("⚫")
        else:
            h_utdrag += 1
            resultat.append("⚪")

    # Lagre til session_state
    st.session_state.simulert = True
    st.session_state.h = h
    st.session_state.s = s
    st.session_state.h_utdrag = h_utdrag
    st.session_state.resultat = resultat

# VIS SIMULERINGA HVIS DEN ER GJENNOMFØRT
if st.session_state.get("simulert"):
    st.subheader("Resultat frå simuleringa")
    st.write(" ".join(st.session_state.resultat))

    # Gjetting
    gjett = st.number_input("Kor mange kvite trur du det var i posen?", min_value=0, max_value=n, step=1)

    if st.button("Gjett talet på kvite brikker"):
        h = st.session_state.h
        s = st.session_state.s
        h_utdrag = st.session_state.h_utdrag

        st.markdown("---")
        st.subheader("Fasit og oppsummering")
        st.write(f"Du har gjetta {n - gjett} svarte og {gjett} kvite.")
        st.write(f"Fasit: {s} svarte og {h} kvite.")
        st.write(f"Andel kvite brikker: {h/n:.2%}")
        st.write(f"Kvite i utdraget: {h_utdrag} av {u} → {100*h_utdrag/u:.2f} %")
        st.markdown("© ØG")

#
