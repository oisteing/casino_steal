import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Half-Average Visualizer", layout="centered")

st.title("🎯 Halferage visuals")

# Initialize session state
if "numbers" not in st.session_state:
    st.session_state.numbers = []

# --- Input Form (Enter submits the number) ---
with st.form(key="add_number_form"):
    
    new_number = st.number_input(
        "Velg eit tal mellom 0 og 100",
        min_value=0,
        max_value=100,
        step=1,
        key="number_input"
    )
    submitted = st.form_submit_button("Legg til")

if submitted:
    st.session_state.numbers.append(new_number)

snitt=st.checkbox("Vise halvparten av gjennomsnittet")

# --- Reset Button (outside the form) ---
if st.button("🔁 Nullstill"):
    st.session_state.numbers.clear()

# --- Display Results ---
if st.session_state.numbers:
    avg = sum(st.session_state.numbers) / len(st.session_state.numbers)
    half_avg = avg / 2

    if snitt:
        st.markdown(
            f"### ➗ Halvparten av gjennomsnittet: \n\n <span style='font-size:64px'>{half_avg:.2f}</span>",
            unsafe_allow_html=True
    )

    # Create histogram
    fig, ax = plt.subplots(figsize=(10, 5))
    counts = [st.session_state.numbers.count(i) for i in range(101)]
    ax.bar(range(101), counts, width=1.0, align="center")

    # Add vertical line at half-average
    if snitt:
        ax.axvline(half_avg, color='red', linestyle='--', linewidth=2)
        ax.text(half_avg + 1, max(counts) * 0.9, f'Half-avg\n{half_avg:.2f}', color='red')

    ax.set_xlabel("Verdi")
    ax.set_ylabel("Frekvens")
    ax.set_title("Frekvens for valgte tall (0–100)")
    ax.set_xlim(0, 100)

    st.pyplot(fig)
else:
    st.write("Kom igjen, legg til nokre tal!")
