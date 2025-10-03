import csv

def mest_utlante_boker(filnavn):
    teller = {}

    with open(filnavn, "r", encoding="utf-8") as f:
        leser = csv.DictReader(f, delimiter="\t")
        for rad in leser:
            try:
                bok = rad["Boktittel"].strip()
                if bok: 
                    if bok in teller:
                        teller[bok] += 1
                    else:
                        teller[bok] = 1
            except:
                continue

    if not teller:
        return []

   
    maks_utlan = max(teller.values())

    
    mest_utlante = [(bok, antall) for bok, antall in teller.items() if antall == maks_utlan]
    mest_utlante.sort(key=lambda x: x[0])  

    return mest_utlante


#Programstart
if __name__ == "__main__":
    resultat = mest_utlante_boker("src/bokutlaan.csv")
    print("Bøker som er lånt ut flest ganger:")
    for bok, antall in resultat:
        print(f" - {bok}: {antall} ganger")