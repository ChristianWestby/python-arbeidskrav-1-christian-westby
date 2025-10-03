
from datetime import datetime

def sjekk_gyldig_dato():
    dato_str = input("Skriv inn en dato (dd/mm/yyyy): ") 
    
    try:
        dato = datetime.strptime(dato_str, "%d/%m/%Y")
        print(f"Datoen {dato_str} er gyldig.")

    except ValueError:
        print(f"Feil: Datoen {dato_str} er ugyldig.Skriv inn datoen med riktig format dd/mm/yyyy.")
        
# Programstart
if __name__ == "__main__":
    sjekk_gyldig_dato()






