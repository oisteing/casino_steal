import streamlit as st
from random import *
from statistics import *

# Ordliste for omsetjing
translations = {
    "Nynorsk": {
        "go": "Køyr",
        "modell": "Modell",
        "intro": "Denne webappen er basert på Kugle-1-2-3, som er presentert i boka Stokastik (Studentliteratur). Programmet var ikkje å finne lenger og eksisterte uansett kun for PC, så eg laga ein web-versjon av det.",
        "tittel": "Kugle kugler  :sunglasses: nline 1.0",
        "typetal": "Typetal",
        "gjennomsnitt": "Gjennomsnitt", 
        "median": "Median",
        "varians": "Varians", 
        "standardavvik": "Standardavvik", 
        "liste over resultat": "Liste over resultat", 
        "raude": "raude",
        "raude og": "raude og",
        "blå": "blå",
        "totalt": "Totalt",
        "modell1": "Denne modellen lar deg legge eit antal raude og blå kuler i ei eske, for så å trekkje ut eit visst antal. Dette kan gjentakast fleire gonger med fleire simuleringar.",
        "modell2": "Denne modellen lar deg trekkje kule etter kule frå eska til du treffer på den første raude kula.",
        "modell3": "Denne modellen lar deg legge eit antal raude og blå kuler i ei eske, for så å trekkje ut ei og ei kule til du har trekt ut alle dei raude.",
        "antall gongar du trekte": "Antal gongar du trekte", 
        "kor mange kuler i eska": "Kor mange kuler er det i eska? (1-10000)",
        "kor mange raude i eska": "Kor mange raude kuler skal det vere i eska?",
        "trekkantall": "Kor mange kuler skal trekkjast ut kvar gong?",
        "legg tilbake": "Skal du kunne leggje attende kula du har trekt ut?",
        "ikkje legg tilbake": "Når du ikkje har tilbakeleggjing kan du ikkje trekkje ut fleire enn du har i eska.",
        "antall simuleringar": "Kor mange simuleringar skal vi kjøre? (1-10000)",
        "antall raude": "Antal raude",
        "antall gongar": "Antal gongar",
        "du måtte trekkje": "Du måtte trekkje",
        "gongar før første": "gongar før du fekk den første raude kula",
        "gongar før alle": "gongar for å trekkje alle dei"
    },
    "Bokmål": {
        "go": "Kjør",
        "modell": "Modell",
        "intro": "Denne webappen er basert på Kugle-1-2-3, som er presentert i boka Stokastik (Studentliteratur). Programmet eksisterte kun for PC, så jeg laget en web-versjon av det.",
        "tittel": "Kule kuler",
        "typetal": "Typetall",
        "gjennomsnitt": "Gjennomsnitt",
        "median": "Median",
        "varians": "Varians", 
        "standardavvik": "Standardavvik", 
        "liste over resultat": "Liste over resultat", 
        "raude": "røde", 
        "raude og": "røde og",
        "blå": "blå",
        "totalt": "Totalt",
        "modell1": "Denne modellen lar deg legge et antall røde og blå kuler i ei eske, for så å trekke ut et visst antall. Dette kan gjentas flere ganger med flere simuleringer.",
        "modell2": "Denne modellen lar deg trekke kule etter kule fra eska til du treffer på den første røde kula.",
        "modell3": "Denne modellen lar deg legge røde og blå kuler i ei eske, for så å trekke ut ei og ei kule til du har trukket alle de røde.",
        "antall gongar du trekte": "Antall ganger du trakk ", 
        "kor mange kuler i eska": "Hvor mange kuler skal det være i eska? (1-10000)",
        "kor mange raude i eska": "Hvor mange røde kuler er det i eska?",
        "trekkantall": "Hvor mange kuler skal du trekke ut hver gang?",
        "legg tilbake": "Skal du kunne legge tilbake kula du har trukket ut?",
        "ikkje legg tilbake": "Når du ikke har tilbakelegging kan du ikke trekke ut flere enn du har i eska.",
        "antall simuleringar": "Hvor mange simuleringer skal vi kjøre? (1-10000)",
        "antall raude": "Antall røde",
        "antall gongar": "Antall ganger",
        "du måtte trekkje": "Du måtte trekke",
        "gongar før første": "ganger før du traff den første røde kula",
        "gongar før alle": "ganger for å trekke alle de"
    },
    "English": {
        "go": "Go!",
        "modell": "Model",
        "intro": "This webapp is based on Kugle 1-2-3, introduced in the book Stokastik (Studentliteratur). This product was only available for PC, so I made a web-based version.",
        "tittel": "C:sunglasses: :sunglasses: lbeans ",
        "typetal": "Mode", 
        "gjennomsnitt": "Average (Mean)",
        "median": "Median",
        "varians": "Variance",
        "standardavvik": "Standard Deviation", 
        "liste over resultat": "Resulting list", 
        "raude": "red",
        "raude og": "red and",
        "blå": "blue",
        "totalt": "In total",
        "modell1": "This model allows you to put a number of red and blue marbles in a box, and then drawing out of certain number of them. This can be repeated any number of times.",
        "modell2": "This model allows you to draw from the box until you hit the first red marble.",
        "modell3": "This model allows you to draw from the box until all red marbles are found.",
        "antall gongar du trekte": "The number of times you drew ",
        "kor mange kuler i eska": "How many marbles should be placed in the box? (1-10000)",
        "kor mange raude i eska": "How many red marbles are placed in the box?",
        "trekkantall": "How many marbles to draw from the box each time?",
        "legg tilbake": "Should you allow for repetitions?",
        "ikkje legg tilbake": "If you don't use repetitions you can not draw more marbles than are in the box.",
        "antall simuleringar": "How many simulations do you want to run? (1-10000)",
        "antall raude": "Number of reds",
        "antall gongar": "Number of times",
        "du måtte trekkje": "You had to draw",
        "gongar før første": "times before hitting the first red marble",
        "gongar før alle": "times to find alle the"
    }
}

options = ["Nynorsk", "Bokmål", "English"]
selection = st.sidebar.radio(" ", options)
#st.sidebar.write("(c) oisteing")
st.title(translations[selection]['tittel'])
st.sidebar.write(translations[selection]['intro'])
#st.sidebar.write("Sjekk kombinatorikk-appen og:")
#st.sidebar.page_link("https://ezudqix98qb6m3zykxcxug.streamlit.app/", label="Kombinatorikk",)
#st.logo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXL74BGleH6oFgRBkKovXDFNTb0h5U46mhnQ&s")
#st.logo("https://www.oisteing.com/images/logowww.png", link="https://www.oisteing.com")
#st.logo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXL74BGleH6oFgRBkKovXDFNTb0h5U46mhnQ&s", link="https://www.oisteing.com")


def gjennomsnitt(lst):
  return mean(lst)

def typetal(lst):
  return mode(lst)

def varians(lst):
  return(variance(lst))

def skriv_regnskap(lst, modell, numsim):
  st.divider()
  if len(lst)<250:
    st.text(translations[selection]['liste over resultat']+":")
    st.text(lst)
  st.write(translations[selection]['typetal'],f": {typetal(lst)}")
  st.write(translations[selection]['gjennomsnitt'], f": {gjennomsnitt(lst): .2f}")
  if numsim>1:
    var=variance(lst)
    std=var**0.5
    st.write(translations[selection]['varians'], f": {var: .2f}")
    st.write(translations[selection]['standardavvik'],f": {std: .2f}")
  st.text("")
  if modell==1:
    if antall_som_trekkes<50: #Skriv ut kor mange gongar dei forskjellige verdiane dukket opp, dersom det er færre enn 50 kuler
     for k in range(antall_som_trekkes+1):
       st.write(translations[selection]['antall gongar du trekte'], k, translations[selection]['raude'], " : ", sum(1 for i in lst if i  == k),"  ")
  
def trekk(antall=1):
  global raude
  global blaa
  global resultatstreng
  if tilbakelegging==True:
    for i in range(antall):
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        raude = raude+1
        #resultatstreng=resultatstreng+" **:red[R]**"
        resultatstreng=resultatstreng+" 🔴"
      else:
        resultatstreng=resultatstreng+" 🔵"
        blaa=blaa+1
  else:
    for i in range(antall):
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        raude = raude+1
        resultatstreng=resultatstreng+" 🔴"
      else:
        resultatstreng=resultatstreng+" 🔵"
        blaa=blaa+1
      eske.pop(kulenr-1)
      
tab1, tab2, tab3 = st.tabs([translations[selection]['modell']+" 1", translations[selection]['modell']+" 2", translations[selection]['modell']+" 3"])

with tab1:
  st.text(translations[selection]['modell1'])
  
  kuler_i_esken = int(st.number_input(translations[selection]['kor mange kuler i eska'], min_value=1, max_value=10000, value=6))
  raude_i_esken = int(st.number_input(translations[selection]['kor mange raude i eska']+" (1-"+f"{kuler_i_esken})", min_value=1, value=1, max_value=kuler_i_esken))
  antall_som_trekkes = int(st.number_input(translations[selection]['trekkantall'], min_value=1, value=6))
  tilbakelegging=st.checkbox(translations[selection]['legg tilbake'], key=11, value=True)
  antall_simuleringar = int(st.number_input(translations[selection]['antall simuleringar'], min_value=1, max_value=10000, value=10))
  resultater=[]

  if st.button(translations[selection]['go'], key=1):
      if not tilbakelegging and antall_som_trekkes>kuler_i_esken:
        st.warning(translations[selection]['ikkje legg tilbake'], icon="⚠️")
        #st.write(translations[selection]['ikkje legg tilbake'])
      else:      
        for j in range(antall_simuleringar):
          resultatstreng=" "
          eske = []
          for i in range(kuler_i_esken):
            eske.append(0)
          for j in range(raude_i_esken):
            eske[j]=eske[j]+1
          raude=0
          blaa=0
          trekk(antall_som_trekkes)
          if antall_simuleringar<11 and antall_som_trekkes<500:
            st.markdown(resultatstreng)
            st.write(translations[selection]['totalt'], raude, translations[selection]['raude og'], blaa, translations[selection]['blå']+".")
          resultater.append(raude)
        skriv_regnskap(resultater, 1, antall_simuleringar)

        #kat=[]
        val=[]
        for k in range(antall_som_trekkes+1):
          a = sum(1 for i in resultater if i  == k) 
          #kat.append(k)
          val.append(a)
        st.bar_chart(val, x_label=translations[selection]['antall raude'], y_label=translations[selection]['antall gongar'], )
  
with tab2:
  def trekk_mod2():
    if tilbakelegging2==True:
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        return True
      else:
        return False
    else:
      kulenr=randint(1,len(eske))
      if eske[kulenr-1]==1:
        return True
      else:
        eske.pop(kulenr-1)
        return False
  st.text(translations[selection]['modell2'])
  kuler_i_esken2 = int(st.number_input(translations[selection]['kor mange kuler i eska'], min_value=1, value=100, key=21))
  raude_i_esken2 = int(st.number_input(translations[selection]['kor mange raude i eska']+" (1-"+f"{kuler_i_esken2})" ,min_value=1, max_value=kuler_i_esken2, key=22))
  tilbakelegging2=st.checkbox(translations[selection]['legg tilbake'], key=5, value=False)
  antall_simuleringar2 = int(st.number_input(translations[selection]['antall simuleringar'], min_value=1, max_value=10000, value=2, key=23))
  resultater2=[]

  if st.button("Go!", key=2):
    for i in range(antall_simuleringar2):
      teller=1
      resultatstreng2=""
      eske = []
      for k in range(kuler_i_esken2):
        eske.append(0)
      for j in range(raude_i_esken2):
        eske[j]=eske[j]+1
      while not trekk_mod2():
        if antall_simuleringar2<30:
          resultatstreng2=resultatstreng2+" 🔵"
        teller=teller+1
      resultater2.append(teller)
      if antall_simuleringar2<30:
        resultatstreng2=resultatstreng2+" 🔴"
        st.write(resultatstreng2)
        if antall_simuleringar2<20:
          st.write(translations[selection]['du måtte trekkje'],teller, translations[selection]['gongar før første'])
    skriv_regnskap(resultater2, 2, antall_simuleringar2)
    
    #kat=[]
    val=[]
    for k in range(max(resultater2)+1):
        a = sum(1 for i in resultater2 if i  == k) 
        #kat.append(k)
        val.append(a)
    
    st.bar_chart(val, x_label=translations[selection]['antall gongar du trekte'], y_label=translations[selection]['antall gongar'], )

with tab3:
  st.text(translations[selection]['modell3'])
  
  def trekk3():
    kulenr=randint(1,len(eske))
    if eske[kulenr-1]==1:
      eske.pop(kulenr-1)
      return True
    else:
      eske.pop(kulenr-1)
      return False

  kuler_i_esken3 = int(st.number_input(translations[selection]['kor mange kuler i eska'], min_value=1, max_value=10000, value=100, key=31))
  raude_i_esken3 = int(st.number_input(translations[selection]['kor mange raude i eska']+f" (max {kuler_i_esken3})",min_value=1, max_value=kuler_i_esken3, value=1, key=32))
  antall_simuleringar3 = int(st.number_input(translations[selection]['antall simuleringar'], key=33, min_value=1, value=2, max_value=10000))
  resultater3=[]

  if st.button(translations[selection]['go'], key=3):
    for i in range(antall_simuleringar3):
      resultatstreng3=""
      tell_raude=0
      antall_trekk=0
      eske = [] #setter opp eska
      for k in range(kuler_i_esken3):
        eske.append(0)
      
      for j in range(raude_i_esken3):
        eske[j]=eske[j]+1
      

      while tell_raude<raude_i_esken3:
        if trekk3():
          tell_raude=tell_raude+1
          resultatstreng3=resultatstreng3+" 🔴"
          
        else:
          resultatstreng3=resultatstreng3+" 🔵"
          
        antall_trekk=antall_trekk+1

      resultater3.append(antall_trekk)
      
      if antall_simuleringar3<20:
        st.write(resultatstreng3)
        st.write(translations[selection]['du måtte trekkje']+f" {antall_trekk} "+translations[selection]['gongar før alle']+f" {raude_i_esken3} "+translations[selection]['raude']+".") 
    
    skriv_regnskap(resultater3, 3, antall_simuleringar3)
    
    val=[]
    for k in range(max(resultater3)+1):
        a = sum(1 for i in resultater3 if i  == k) 
        val.append(a)
    
    st.bar_chart(val, x_label=translations[selection]['antall gongar du trekte'], y_label=translations[selection]['antall gongar'], )
