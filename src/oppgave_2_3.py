def list_splitting():
    
        personer = ["Cecilie", 28, "Bjørn", 30,"Tor", 24,"Anna", 25]

        navn = []
        alder = []
        for i in range(0,len(personer),2):
                navn.append(personer[i])
                alder.append(personer[i + 1])
        print("Navn-liste:", navn)
        print("Alder-liste:", alder)

def finn__alder_for_navn():
    navn_liste = ["Cecilie", "Bjørn", "Tor", "Anna"]
    alder_liste = [28, 30, 24, 25]
    navn = input("Skriv inn et navn: ")
    if navn in navn_liste:
        index = navn_liste.index(navn)
        print(f"{navn} er {alder_liste[index]} år gammel.")
    else:
        print(f"{navn} finnes ikke i listen.")
    
    

#Programstart
if __name__ == "__main__":
    list_splitting()
    finn__alder_for_navn()