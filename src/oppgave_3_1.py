def sjekk_om_ipv4_adresse_er_gyldig(ip_adresse):
    deler = ip_adresse.split(".")
    
    if len(deler) != 4:
        return False

    for del_streng in deler:
        if not del_streng.isdigit():
            return False
        
        tall = int(del_streng)

    
        if tall < 0 or tall > 255:
            return False

    return True


# Programstart
if __name__ == "__main__":
    ip = input("Skriv inn en IPv4-adresse: ")
    if sjekk_om_ipv4_adresse_er_gyldig(ip):
        print(f"{ip} er en gyldig IPv4-adresse")
    else:
        print(f"{ip} er en ugyldig IPv4-adresse")