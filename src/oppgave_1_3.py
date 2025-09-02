# src/oppgave_1_3.py

def vis_multiplikasjonstabell():
    try:
        tall = int(input("Skriv inn et tall for å se multiplikasjonstabellen (1-10): "))
    except ValueError:
            print("Ugyldig input. Du må skrive inn et heltall og tallet må være mellom 1 og 10.")
            return
    print(f"\nMultiplikasjonstabell for {tall}:\n")
    for i in range(1, 11):
            resultat = tall * i
            print(f"{tall} x {i} = {resultat}")
            
            
# Programstart
if __name__ == "__main__":
    vis_multiplikasjonstabell()
