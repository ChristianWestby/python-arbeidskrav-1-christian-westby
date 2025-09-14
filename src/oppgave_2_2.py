def list_splitting():
    
        personer = ["Cecilie", 28, "Bjørn", 30,"Tor", 24,"Anna", 25]

        navn = []
        alder = []
        for i in range(0,len(personer),2):
                navn.append(personer[i])
                alder.append(personer[i + 1])
        print("Navn-liste:", navn)
        print("Alder-liste:", alder)


#Programstart
if __name__ == "__main__":
    list_splitting()