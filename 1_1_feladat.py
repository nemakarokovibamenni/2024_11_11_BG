'''Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket 
írja ki a képernyőre!Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! 
A program a bekért neveket írja ki a képernyőre!Készíts egy programot, amely a felhasználótól keresztneveket kér be 
egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!'''


nevek = []
folytat = True
def a():
    while folytat:
        print(len(nevek))
        if len(nevek) >= 2:
            folytat = False
        nev = input('Kérlek adj meg egy keresztnevet: ')
        if nev == '':
            folytat = False
        nevek.append(nev)

    print(nevek)





def b():
   for i in range(3):
    nev= input('Kérlek adj meg egy keresztnevet: ')
    if nev == '':
        break
    nevek.append(nev)

    print(nevek)


#a()
b()