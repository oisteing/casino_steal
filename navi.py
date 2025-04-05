import streamlit as st

pages = {
    "Simuleringer": [
        st.Page("halfmean.py", title="Half of the average"),
        st.Page("trekke.py", title="Trekke brikker"),
    ],
    "Ressurser": [
        st.Page("kuglekugler_online.py", title="Kule kuler"),
        st.Page("kombikalk2.py", title="Kombinatorikk"),
        st.Page("binomisk.py", title="Binomialfordeling")
    ],
}

pg = st.navigation(pages)
pg.run()