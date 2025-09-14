def finn_det_laveste_tallet_i_listen():
    tall_liste = [44, 60, 65, 89,44, 23, 5]
    if not tall_liste:
        print ("Listen er tom.")
        return
    
    laveste_tall = min(tall_liste)
    
    print (f"Det laveste_tallet_i_listen_er: {laveste_tall}")
    
#Programstart
if __name__ == "__main__":
    finn_det_laveste_tallet_i_listen()