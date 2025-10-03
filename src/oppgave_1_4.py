def bytt_plass_på_to_elementer_i_liste():
    frukt = ["eple", "banan", "kiwi", "druer", "appelsin"]
    print(f"Opprinnelig liste: {frukt}")
    
    try:
        index1 = int(input("Skriv inn plass nr til den første frukten du vill flytte: "))
        index2 = int(input("Skriv inn plass nr til den andre frukten du vill flytte: "))

   
        if index1 < 0 or index1 >= len(fruits) or index2 < 0 or index2 >= len(fruits):
            print("Feil: En eller begge indekser er utenfor gyldig område.")
            return

        
        frukt[index1], frukt[index2] = frukt[index2], frukt[index1]
        print (f"Oppdatert liste: {frukt}")
  
    except ValueError:
        print("ugyldig input. Du må skrive inn heltall som indexser.")
        
        
if __name__ == "__main__":
    bytt_plass_på_to_elementer_i_liste()
    
