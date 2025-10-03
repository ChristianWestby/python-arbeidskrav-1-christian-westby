def vis_multiplikasjonstabell_i_intervall():
    try: 
        tall = int(input("Skriv inn et tall du vill at tabellen skal være for!"))
        start = int(input("Skriv inn startverdi for intervallet!"))
        slutt = int(input("Skriv inn sluttverdi for intervallet!"))
        
        if start > slutt:
            print("Error: Startverdi må være mindre enn eller lik sluttverdi.")
            return
        
        print(f"Multiplikasjonstabell for {tall} fra {start} til {slutt}:\n")
        
        for i in range(start, slutt + 1):
            print(f"{tall} x {i} = {tall * i}")

    except ValueError:
        print("Ugyldig input. Vennligst skriv inn heltall.")

# Programstart
if __name__ == "__main__":
    vis_multiplikasjonstabell_i_intervall()
