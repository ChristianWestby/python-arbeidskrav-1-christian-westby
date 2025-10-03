
def test_funksjon(funksjon, args, forventet):
    resultat = funksjon(*args)

    if resultat == forventet:
        print(f"Test bestått: {funksjon.__name__}{args} = {resultat}")
        return True
    else:
        print(f"Test feilet: {funksjon.__name__}{args} = {resultat}, forventet {forventet}")
        return False


def legg_sammen_disse_tallene(a, b):
    return a + b

#Programstart
if __name__ == "__main__":
    test_funksjon(legg_sammen_disse_tallene, (2, 3), 5)  
    test_funksjon(legg_sammen_disse_tallene, (2, 4), 8)  