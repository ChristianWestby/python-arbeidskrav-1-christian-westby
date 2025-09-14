def finn_summen_av_tall_i_listen():
    tall_liste = 20, 27, 45.55, 45, 55 
    print(f"Dette er listen av tall vi ønsker å legge sammen: {tall_liste}")
           
    if not tall_liste:
        print ("Det er ikke noe liste, jeg tulla med deg!")
        return
    total_desimaler = 0
    for tall in tall_liste:
        total_desimaler += tall
        
    
    print (f"Summen av tallene i listen er: {total_desimaler}")
  
    total_heltall = 0
     
    for tall_heltall in tall_liste:
        total_heltall += int (tall_heltall)

    print (f"Dette er summen av tallene avrundet: {int (total_heltall)}")
        
        
#Programstart
if __name__ == "__main__":
    finn_summen_av_tall_i_listen()