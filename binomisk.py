import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.stats import binom

st.title("Binomisk Sannsynlighetsfordeling")

# Input fra bruker
n = st.number_input("Antall forsøk (n)", min_value=1, value=10, step=1)
p = st.number_input("Sannsynlighet for suksess (p)", min_value=0.0, max_value=1.0, value=0.5)

# Beregn binomisk sannsynlighetsfordeling
x = np.arange(0, int(n) + 1)
pmf = binom.pmf(x, n, p)



# Plotting
fig, ax = plt.subplots()
ax.plot(x, pmf, 'bo', ms=8, label='binom.pmf')
ax.vlines(x, 0, pmf, colors='b', lw=5, alpha=0.5)
ax.set_xlabel('Antall suksesser')
ax.set_ylabel('Sannsynlighet')
ax.set_title(f'Binomisk fordeling (n={n}, p={p})')
ax.legend()

st.pyplot(fig)

# Lag en pandas DataFrame for å vise resultatene i tabellformat
data = pd.DataFrame({
    "Antall suksesser": x,
    "Sannsynlighet": pmf
})

st.subheader("Beregnede sannsynligheter")
st.dataframe(data)