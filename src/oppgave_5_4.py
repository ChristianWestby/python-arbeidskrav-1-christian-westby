import csv

def ikke_levert(filnavn):
    resultat = []

    with open(filnavn, "r", encoding="utf-8") as f:
        leser = csv.DictReader(f, delimiter="\t")
        for rad in leser:
            try:
                if rad["Tilbakelevert"].strip().lower() == "nei":
                    bok = rad["Boktittel"].strip()
                    fornavn = rad["Fornavn"].strip()
                    etternavn = rad["Etternavn"].strip()
                    resultat.append(f"{bok} (lånt av {fornavn} {etternavn})")
            except:
                continue  

    return resultat


#Programstart
if __name__ == "__main__":
    bøker = ikke_levert("src/bokutlaan.csv")
    print("Bøker som ikke ble levert tilbake:")
    for b in bøker:
        print(" -", b)