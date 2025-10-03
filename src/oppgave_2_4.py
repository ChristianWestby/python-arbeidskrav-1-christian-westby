def finn_hoyeste_alder_i_liste():
    alder_liste = (28, 30, 24, 25)
    
    if not alder_liste:
        print("Listen er tom.")
        return
    
    hoyeste_alder = max(alder_liste)
    print(f"Hoyeste alder i listen er: {hoyeste_alder}år")
    
#Programstart
if __name__ == "__main__":
    finn_hoyeste_alder_i_liste()
        