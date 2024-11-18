'''A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. 
A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!'''

#ha a szín nem szerepel a listában egészítsd ki a listát a színne, majd printeld is ki az új listát

színek = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']
print(színek)

szin = input('Adj meg egy színt!\t')
# if szin in színek:
# 	print('A megadott szín szerepel a listában.')
# else:
#     print('A megadott szín nem szerepel a listában.')
#     színek.append(szin)

# print('A lista új lista színei:')
# for szin in színek:
# 	print(szin, end=' ')

#Töröld a megadott színt a listából.
if szin in színek:
    színek.remove(szin)
else:
    print('Nincsen ilyen szín a megadott listában! Legközelebb légy figyelmesebb 😉')
print(színek)