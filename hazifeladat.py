'''Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt 
hagyja figyelmen kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért 
neveket írja ki a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!'''


def main():

    szavak = []

    while True:
        szo = input("Adj meg egy szót: ").strip()

        
        if szo == "":
            break

        
        if szo[0].lower() == 'a':
            szavak.append(szo)
        else:
            print(f"A '{szo}' nem kezdődik 'a'-val, figyelmen kívül hagyva!")

    print("\nA tárolt szavak:")
    for szo in szavak:
        print(szo)


if __name__ == "__main__":
    main()




