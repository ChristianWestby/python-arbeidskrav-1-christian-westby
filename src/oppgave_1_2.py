# src/oppgave_1_2.py
def sammenlign_setninger():
    setning1 = input("Skriv inn den første setningen: ")
    setning2 = input("Skriv inn den andre setningen: ")

    lengde1 = len(setning1)
    lengde2 = len(setning2)

    if lengde1 > lengde2:
        print("Den første setningen er lengre enn den andre.")
        print(f"Lengde: {lengde1} tegn")
    elif lengde2 < lengde1:
        print("Den andre setningen er lengre enn den første.")
    else:
        print("Begge setningene har lik lengde.")
        print(f"Lengde: {lengde1} tegn")
        
#Programstart
if __name__ == "__main__":
    sammenlign_setninger()
