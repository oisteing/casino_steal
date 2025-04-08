import streamlit as st

st.set_page_config(page_title="Faktaark - Sannsynlighet og Statistikk")

st.title("📘 Faktaark: Sannsynlighet og Statistikk")

# -----------------------------
st.header("🧠 Sannsynlighet")

st.subheader("Addisjonssetningen")
st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")

st.subheader("Betinget sannsynlighet")
st.latex(r"P(A \mid B) = \frac{P(A \cap B)}{P(B)}")

st.subheader("Bayes' formel")
st.latex(r"""
P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)} = 
\frac{P(B \mid A)P(A)}{P(B \mid A)P(A) + P(B \mid \overline{A})P(\overline{A})}
""")

# -----------------------------
st.header("📋 Utvalg")

st.markdown("Gjør vi et utvalg av størrelse $r$ fra en mengde $n$, er antall kombinasjoner:")

st.markdown("""
|                      | Med tilbakelegging      | Uten tilbakelegging        |
|----------------------|--------------------------|-----------------------------|
| **Ordna**            | $n^r$                    | $\\frac{n!}{(n - r)!}$      |
| **Uordna**           | $\\binom{n + r - 1}{r}$  | $\\binom{n}{r}$             |
""", unsafe_allow_html=True)

# -----------------------------
st.header("📊 Statistiske mål")

st.subheader("Varians og standardavvik")

st.markdown("**For $n$ enkeltobservasjoner:**")
st.latex(r"s^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2")

#st.markdown("**Forventningsrett estimator:**")
#st.latex(r"s^2 = \frac{1}{n - 1} \sum_{i=1}^n (x_i - \bar{x})^2")

#st.markdown("**Forventning, varians og standardavvik for en stokastisk variabel $X$:**")
#st.latex(r"""
#\mu = \mathrm{E}(X) = \sum_{\text{alle } x_i} x_i \cdot P(X = x_i)
#""")
#st.latex(r"""
#\sigma^2 = \mathrm{Var}(X) = \sum_{\text{alle } x_i} (x_i - \mu)^2 \cdot P(X = x_i)
#""")
#st.latex(r"""
#\sigma = \sqrt{\mathrm{Var}(X)}
#""")


# -----------------------------
st.header("🧮 Binomialkoeffisienten")
st.latex(r"\binom{n}{r} = \frac{n!}{(n - r)! r!}")

# -----------------------------
st.header("🎲 Sannsynlighetsfordelinger")

st.subheader("Binomisk fordeling")
st.latex(r"P(X = x) = \binom{n}{x} p^x (1 - p)^{n - x}")
st.latex(r"\mathrm{E}(X) = np, \quad \mathrm{Var}(X) = np(1 - p)")

st.subheader("Hypergeometrisk fordeling")
st.latex(r"""
P(X = x) = \frac{\binom{S}{x} \binom{N - S}{n - x}}{\binom{N}{n}}
""")
st.latex(r"""
\mathrm{E}(X) = np, \quad 
\mathrm{Var}(X) = np(1 - p) \cdot \frac{N - n}{N - 1}, \quad 
p = \frac{S}{N}
""")

