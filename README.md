# Python Arbeidskrav 1 – Christian Westby

Dette prosjektet inneholder løsninger til **Arbeidskrav 1 i Python** (Gokstad Akademiet, høst 2025).  
Alle oppgavene fra oppgaveteksten er løst i separate `.py`-filer, og ligger under mappen `src/`.

---

## 📂 Filstruktur
src/
│── oppgave_1_1.py
│── oppgave_1_2.py
│── oppgave_1_3.py
│── oppgave_1_4.py
│── oppgave_1_5.py
│── oppgave_2_1.py
│── oppgave_2_2.py
│── oppgave_2_3.py
│── oppgave_2_4.py
│── oppgave_2_5.py
│── oppgave_2_6.py
│── oppgave_3_1.py
│── oppgave_3_2.py
│── oppgave_3_3.py
│── oppgave_3_4.py
│── oppgave_4_1.py
│── oppgave_4_2.py
│── oppgave_5_1.py
│── oppgave_5_2.py
│── oppgave_5_3.py
│── oppgave_5_4.py
│── oppgave_5_5.py
bokutlaan.csv   ← brukt i oppgave 5

---

## 🚀 Hvordan kjøre
1. Sørg for at du er i prosjektmappen.  

2. Kjør en fil i terminalen slik:  
   ```bash
   python src/oppgave_2_3.py

3.	Oppgave 5 bruker bokutlaan.csv. Denne må ligge i src/-mappen.

Kort om oppgavene
Oppgave 1 – grunnleggende løkker, input og output
Oppgave 2 – lister og dictionary
Oppgave 3 – funksjoner, IPv4-sjekk, dato, fargekoder og enkel test-funksjon
Oppgave 4 – filhåndtering (opprette og sortere filer)
Oppgave 5 – analyse av bokutlaan.csv (forlengelser, sjanger, gjennomsnittlig lånetid, ikke leverte bøker, mest utlånte bøker)

Bruk av AI
AI (ChatGPT) er brukt kun som læringsstøtte.
Jeg har ofte bedt om forklaringer og enklere formuleringer av oppgavetekstene, og fått forslag til struktur.
Koden er deretter skrevet og tilpasset manuelt, med fokus på enkelhet og forståelse.
Noen forklaringer og diskusjoner med AI er derfor ikke inkludert i selve koden.
Alle filer i src/ er skrevet, tilpasset og testet i VS Code av meg.

Prompts og svar brukt i koden

I starten brukte jeg ChatGPT mest for å forklare konsepter (løkker, dictionaries, isdigit(), osv.).
Underveis ba jeg også om enkle kodeforslag til utgangspunkt (skjelett) som jeg deretter tilpasset selv.

Eksempel på typiske prompts:
“Kan du forklare hva for i in range(0, len(personer), 2) betyr?”
“Lag et utgangspunkt for oppgave 3.1 – sjekke IPv4-adresse”
“Hva betyr strptime og hvorfor brukes det?”

Eksempel på typiske AI-svar som ble brukt:
Forklaringer på hvordan range fungerer.
Skjelettkode for IPv4-sjekk, der jeg selv tilpasset feilmeldinger og input.
Forslag på hvordan bruke csv.DictReader i oppgave 5, som jeg manuelt tilpasset til datasettet.

# PromptLog – Dokumentasjon av AI-bruk

Denne filen inneholder utvalgte **prompts og svar** fra ChatGPT som har bidratt direkte til koden i dette arbeidskravet.  
Diskusjoner som kun var konseptuelle (teori og læringsstøtte) er ikke tatt med, slik retningslinjene åpner for.  

---

## Eksempel 1 – Oppgave 2.2 (splitte liste)
**Prompt:**
> "kan jeg bruke den samme koden uten å måtte skrive hele navnlisten igjen. Kan jeg hente den ut i andre def med f.eks bare navn-liste som jeg lagde i første def?"

**Svar (utdrag):**
> "For å gjenbruke samme navn-liste og alder-liste i flere funksjoner kan du definere dem som egne variabler utenfor funksjonene, slik at de blir tilgjengelige i begge."

---

## Eksempel 2 – Oppgave 3.1 (IPv4-sjekk)
**Prompt:**
> "skriv 3.1 igjen men med denne teksten: `def sjekk_om_ipv4_adresse_er_gyldig():`"

**Svar (utdrag):**
> "Her er en enkel funksjon som sjekker om en streng er en gyldig IPv4-adresse. Den sjekker at adressen består av fire deler, at alle delene er heltall, og at de er mellom 0 og 255."

---

## Eksempel 3 – Oppgave 3.2 (dager mellom datoer)
**Prompt:**
> “hvorfor skal det være nødvendig å gjøre om til heltall? hvis det er komma feil??
og hva står isdigit() for og når brukes den?”

**Svar (utdrag):**
> “Når vi konverterer til heltall med int(), sørger vi for at delen faktisk kan behandles som et tall, ikke bare som tekst. Hvis noen skriver 192.168.0.a, vil int() gi feilmelding og vi fanger opp ugyldig input.
isdigit() brukes for å sjekke om en streng kun består av talltegn (0–9). Det er et første filter, men vi må fortsatt gjøre int()-konverteringen etterpå.”

---

## Eksempel 4 – Oppgave 5.1 (csv)
**Prompt:**
> "men hvor henter du filen i koden her?"

**Svar (utdrag):**
> "I koden kalles `summer_forlengelser("bokutlån.csv")`. Det betyr at programmet forventer at filen `bokutlån.csv` ligger i samme mappe som scriptet, eller at du oppgir en full sti."

---

## Kommentar
- De fleste filene i `src/` er skrevet manuelt, men ChatGPT ble brukt til å forklare kode og foreslå utgangspunkt.  
- Eksempelvis ble skeleton-kode foreslått for `rgb_til_hex`, men input-håndtering og feilmeldinger ble tilpasset manuelt.  
- I CSV-oppgavene fikk jeg forslag på `csv.DictReader`, men håndteringen av tall, feilverdier og feilmeldinger ble gjort etter egen testing.  

---
Alle ferdige .py-filer er manuelt bearbeidet og testet i terminalen.


Refleksjon

Gjennom oppgavene har jeg lært å:
Jobbe strukturert med Python-filer i VS Code
Bruke git og GitHub til versjonskontroll
Skille mellom lister, dictionaries og funksjoner
Bruke csv-modulen til å lese og analysere data
Håndtere input, feilmeldinger og output på en tydelig måte


