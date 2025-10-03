import csv

def beregn_boker_per_sjanger(filnavn):
    teller = {}
    with open(filnavn, "r", encoding="utf-8") as f:
        leser = csv.DictReader(f, delimiter="\t")
        for rad in leser:
            sjanger = rad["Sjanger"].strip()
            if sjanger:  
                if sjanger in teller:
                    teller[sjanger] += 1
                else:
                    teller[sjanger] = 1

    print("Antall bøker per sjanger:")
    for sjanger, antall in teller.items():
        print(f" - {sjanger}: {antall}")


#Programstart
if __name__ == "__main__":
    beregn_boker_per_sjanger("src/bokutlaan.csv")