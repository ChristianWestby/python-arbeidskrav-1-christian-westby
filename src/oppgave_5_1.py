import csv

def summer_forlengelser(filnavn):
    total = 0
    with open(filnavn, "r", encoding="utf-8") as f:
        leser = csv.DictReader(f, delimiter="\t")  
        for rad in leser:
            try:
                dager = int(rad["Forlenget"].strip())
                total += dager
            except:
                continue
    print("Total antall forlengede dager:", total)

#Programstart
if __name__ == "__main__":
    summer_forlengelser("src/bokutlaan.csv")