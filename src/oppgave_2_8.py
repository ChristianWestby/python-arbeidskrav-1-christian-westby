def tell_antall_like_navn():
    navn_liste = ["Cecilie", "Bjørn", "Tor", "Cecilie", "Anna", "Anna", "Cecilie", "Atle"]
    if not navn_liste:
        print("Listen er tom eller finnes ikke.")
        return

    navn = input("Skriv inn et navn for å sjekke antall forekomster i listen: ")
    antall_forekomster = navn_liste.count(navn)
    print (f"{navn} forekommer {antall_forekomster} ganger i denne listen.")
    if antall_forekomster == 0:
        print (f"{navn} finnes ikke i listen.")



#Programstart
if __name__ == "__main__":
    tell_antall_like_navn()