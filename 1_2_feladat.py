'''1.2 Feladat
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, 
írja ki az addig megadott neveket, és lépjen ki.'''

nevek = []

folytat = True
while folytat:
    print(len(nevek))
    if len(nevek) >= 3:
        folytat = False
    nev = input('Kérlek adj meg egy keresztnevet: ')
    if nev == "":
        folytat = False
    nevek.append(nev)

print(nevek)