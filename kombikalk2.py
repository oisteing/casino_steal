from math import *
import streamlit as st


#a=1
#b=1
def ordna_uten(n,r):
    return(int(factorial(n)/factorial(n-r)))

def ordna_med(n,r):
    return(int(n**r))

def uordna_uten(n,r):
    return(int(factorial(n)/(factorial(n-r)*factorial(r))))

def uordna_med(n,k):
    return(int(factorial(n+k-1)/(factorial(n-1)*factorial(k))))

#Sidebar
options = ["Nynorsk", "Bokmål"]
selection = st.sidebar.radio(" ", options)
st.sidebar.write("(c)2025 oisteing")

# Dictionary for translations
translations = {
    "Nynorsk": {
        "vel_modell": "Vel modell:",
        "intro": "Denne webappen er basert på dei fire tellemåtane i kombinatorikk.",
        "ordna": "Ordna utval",
        "uordna": "Uordna utval",
        "utan": "utan tilbakeleggjing",
        "med": "med tilbakeleggjing",
        "ordna_utan": "Ordna utval utan tilbakeleggjing",
        "ordna_med": "Ordna utval med tilbakeleggjing",
        "uordna_utan": "Uordna utval utan tilbakeleggjing",
        "uordna_med": "Uordna utval med tilbakeleggjing",
        "ordna_utan_tekst": "Her skal du gjere r valg på ei mengd som har n moglege når du starter, men der du ikkje legg tilbake.  \nSkriv inn n og så r",
        "ordna_med_tekst": "Da skal du gjere r valg ut frå n moglegheitar.  \n Eksempel er den gammaldagse fotballkupongen. Skriv inn n og så r",
        "uordna_utan_tekst": "Her skal du gjere r valg på ei mengd som har n moglege når du starter, men der du ikkje legg tilbake. Eksempel er lottokupongen. \nSkriv inn n og så r",
        "uordna_med_tekst": "Her skal du gjere r valg på ei mengd som har n moglege, og du legg tilbake det du trekkjer ut.  \nSkriv inn n og så r",
    },
    "Bokmål": {
        "vel_modell": "Velg modell:",
        "intro": "Denne webappen er basert på de fire tellemåtene i kombinatorikk.",
        "ordna": "Ordnet utvalg",
        "uordna": "Uordnet utvalg",
        "utan": "uten tilbakelegging",
        "med": "med tilbakelegging",
        "ordna_utan": "Ordnet utvalg uten tilbakelegging",
        "ordna_med": "Ordnet utvalg med tilbakelegging",
        "uordna_utan": "Uordnet utvalg uten tilbakelegging",
        "uordna_med": "Uordnet utvalg med tilbakelegging",
        "ordna_utan_tekst": "Her skal du gjøre r valg på en mengde som har n mulige når du starter, men der du ikke legger tilbake.  \nSkriv inn n og så r",
        "ordna_med_tekst": "Her skal du foreta r valg på en mengde som har n mulige. Her legger du tilbake det du trekker ut.  \nSkriv inn n og så r",
        "uordna_utan_tekst": "Her skal du ta r valg på en mengde som har n mulige når du starter, men der du ikke legger tilbake.  \nSkriv inn n og så r",
        "uordna_med_tekst": "Her skal du foreta r valg på en mengde som har n mulige, men her legger du tilbake det du trekker ut.  \nSkriv inn n og så r",
    }
}

st.title("Kombokalk online")
st.sidebar.write(translations[selection]['intro'])

#st.logo("https://www.oisteing.com/images/logowww.png", link="https://www.oisteing.com")
#st.logo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXL74BGleH6oFgRBkKovXDFNTb0h5U46mhnQ&s", link="https://www.github.com")

st.divider()


# Radioknapp for utvalgstype
utvalgstype = st.radio(
    translations[selection]['vel_modell'],
    (translations[selection]['uordna'], translations[selection]['ordna'])
)

# Avkrysningsboks for tilbakelegging
med_tilbakelegging = st.checkbox(translations[selection]['med'])

if utvalgstype==translations[selection]['ordna'] and med_tilbakelegging==False:
    #b=1
    st.header(translations[selection]['ordna_utan'])
    st.write(translations[selection]['ordna_utan_tekst'])
    a=int(st.number_input("n: ", key=1, value=1, min_value=1, max_value=100))
    b=int(st.number_input("r: ", value=a, min_value=0, max_value=a))
    translations["Bokmål"]['ordna_utan_svar']="Her har du "+ str(ordna_uten(a,b))+ " muligheter."
    translations["Nynorsk"]['ordna_utan_svar']="Her har du "+ str(ordna_uten(a,b))+ " moglegheitar."
    
    st.write(translations[selection]['ordna_utan_svar'])

if utvalgstype==translations[selection]['ordna'] and med_tilbakelegging==True:
    st.header(translations[selection]['ordna_med'])
    st.write(translations[selection]['ordna_med_tekst'])
    a=int(st.number_input("n: ", key=2, value=1, min_value=1, max_value=100))
    b=int(st.number_input("r: ", value=1, min_value=1))
    translations["Bokmål"]['ordna_med_svar']="Her har du "+ str(ordna_med(a,b))+ " muligheter."
    translations["Nynorsk"]['ordna_med_svar']="Her har du "+ str(ordna_med(a,b))+ " moglegheitar."
    
    st.write(translations[selection]['ordna_med_svar'])

if utvalgstype==translations[selection]['uordna'] and med_tilbakelegging==False:
    st.header(translations[selection]['uordna_utan'])
    st.write(translations[selection]['uordna_utan_tekst'])
    a=int(st.number_input("n: ", value=1, min_value=1, max_value=100))
    b=int(st.number_input("r: ", value=a, min_value=0, max_value=a))
    #Må sette inn keys til dictionaries her, for viss ikkje brukar den a,b=1 fra først i programmet.
    
    translations["Bokmål"]['uordna_utan_svar']="Her har du "+ str(uordna_uten(a,b))+ " muligheter."
    translations["Nynorsk"]['uordna_utan_svar']="Her har du "+ str(uordna_uten(a,b))+ " moglegheitar."
    
    st.write(translations[selection]['uordna_utan_svar'])

if utvalgstype==translations[selection]['uordna'] and med_tilbakelegging==True:
    st.header(translations[selection]['uordna_med'])
    st.write(translations[selection]['uordna_med_tekst'])
    a=int(st.number_input("n: ", value=1, min_value=0, max_value=100))
    b=int(st.number_input("r: ", value=1, min_value=1))
    
    if a>0:
        translations["Bokmål"]['uordna_med_svar']="Her har du "+ str(uordna_med(a,b))+ " muligheter."
        translations["Nynorsk"]['uordna_med_svar']="Her har du "+ str(uordna_med(a,b))+ " moglegheitar."
        st.write(translations[selection]['uordna_med_svar'])