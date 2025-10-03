import csv

def gjennomsnittlig_lanperiode(filnavn):
    total_dager = 0
    antall_boker = 0

    with open(filnavn, "r", encoding="utf-8") as f:
        leser = csv.DictReader(f, delimiter="\t")
        for rad in leser:
            try:
                lan = int(rad["Låneperiode"].strip())
                forleng = int(rad["Forlenget"].strip())
                total_dager += lan + forleng
                antall_boker += 1
            except:
                continue

    if antall_boker > 0:
        gjennomsnitt = total_dager // antall_boker 
        print(f"Gjennomsnittlig låneperiode: {gjennomsnitt} dager")
    else:
        print("Ingen gyldige bøker i datafilen.")


#Programstart
if __name__ == "__main__":
    gjennomsnittlig_lanperiode("src/bokutlaan.csv")