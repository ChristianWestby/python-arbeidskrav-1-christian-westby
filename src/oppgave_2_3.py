def lag_dictionary():
    personer = ["Cecilie", 28, "Bjørn", 30, "Tor", 24, "Anna", 25]

    dictionary = {}
    for i in range(0, len(personer), 2):
        dictionary[personer[i]] = personer[i + 1]

    for navn, alder in dictionary.items():
        print(f"{navn} er {alder} år")

# Programstart
if __name__ == "__main__":
    lag_dictionary()