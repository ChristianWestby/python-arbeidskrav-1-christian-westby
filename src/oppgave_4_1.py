import os
import random
import string

def generer_filer():
    if not os.path.exists("Files"):
        os.makedirs("Files")
    antall_filer = 30
    filtyper = [".txt", ".csv", ".log"]
    
    for i in range(antall_filer):
        navn_lengde = random.randint(5, 10)
        navn = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(navn_lengde))

        filtype = random.choice(filtyper)

        filnavn = os.path.join("Files", navn + filtype)

        with open(filnavn, "w", encoding="utf-8") as f:
            pass  

    print(f"\n{antall_filer} filer generert i mappen 'Files':")
    for fil in os.listdir("Files"):
        print(" -", fil)
    print("Totalt antall filer i mappen nå:", len(os.listdir("Files")))

# Programstart
if __name__ == "__main__":
    generer_filer()