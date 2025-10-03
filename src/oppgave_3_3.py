def rgb_til_hex(red, green, blue):
    return "#{:02X}{:02X}{:02X}".format(red, green, blue)

if __name__ == "__main__":
    r = int(input("Rød (0-255): "))
    g = int(input("Grønn (0-255): "))
    b = int(input("Blå (0-255): "))
    print("Hex-kode:", rgb_til_hex(r, g, b))