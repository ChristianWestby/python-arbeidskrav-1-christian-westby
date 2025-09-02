# src/oppgave_1_1.py

def summer_til_tall():
    try:
        tall = int(input("Skriv inn et positivt heltall: "))
        if tall <= 0:
            print("Du må skrive inn et tall større enn 0.")
            return

        total = 0
        for i in range(1, tall + 1):
            total += i

        print(f"Summen av tallene fra 1 til {tall} er {total}.")
    except ValueError:
        print("Ugyldig input. Vennligst skriv inn et heltall.")


# Programstart
if __name__ == "__main__":
    summer_til_tall()