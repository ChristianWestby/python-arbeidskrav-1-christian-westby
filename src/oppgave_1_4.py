def bytt_plass_på_to_elementer_i_liste():
    fruits = ["eple", "banan", "kiwi", "druer", "appelsin"]
    print(f"Opprinnelig liste: {fruits}")
    
    try:
        index1 = int(input("Skriv inn plass nr til den første frukten du vill flytte: "))
        index2 = int(input("Skriv inn plass nr til den andre frukten du vill flytte: "))

   
        if index1 < 0 or index1 >= len(fruits) or index2 < 0 or index2 >= len(fruits):
            print("Feil: En eller begge indekser er utenfor gyldig område.")
            return

        
        fruits[index1], fruits[index2] = fruits[index2], fruits[index1]
        print (f"Oppdatert liste: {fruits}")
  
    except ValueError:
        print("ugyldig input. Du må skrive inn heltall som indexser.")
        
        
if __name__ == "__main__":
    bytt_plass_på_to_elementer_i_liste()
    
