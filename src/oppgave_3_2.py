from datetime import datetime

def _parse_dato(s):
    s = s.strip().replace(".", "/").replace("-", "/")
    try:
        return datetime.strptime(s, "%d/%m/%Y").date()
    except ValueError:
        return None

def dager_mellom_datoer(d1, d2):
    a = _parse_dato(d1)
    b = _parse_dato(d2)
    if a is None or b is None:
        return None
    return abs((b - a).days)
    
if __name__ == "__main__":
    d1 = input("Første dato (dd/mm/yyyy): ")
    d2 = input("Andre dato (dd/mm/yyyy): ")
    
    dager = dager_mellom_datoer(d1, d2)
    if dager is None:
        print("Ugyldig dato. Bruk format dd/mm/yyyy.")
    else:
        print(f"Antall dager mellom {d1} og {d2}: {dager}")