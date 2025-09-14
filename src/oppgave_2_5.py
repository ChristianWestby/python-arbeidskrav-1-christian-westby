def finn_første_partall_i_liste():
    tall_liste = [7, 9, 11, 13, 20, 24, 28, 29, 31]
    for tall in tall_liste:
        if tall % 2 == 0:
            print(f"Første partall i listen er: {tall}")
            return
    print("Ingen partall funnet.")
    
def finn_første_oddetall_i_listen():   
    tall_liste = [7, 9, 11, 13, 20, 24, 28, 29, 31]
    for tall in tall_liste:
        if tall % 2 != 0:
            print(f"Første oddetall i listen er: {tall}")
            return
#Programstart
if __name__ == "__main__":
    finn_første_partall_i_liste()
    finn_første_oddetall_i_listen()