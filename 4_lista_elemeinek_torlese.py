nyelvek = ['Python', 'GO', 'C', 'C++', 'Java', 'Python', 'HTML']
print(nyelvek)
# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
nyelvek.pop()
print(nyelvek)
torolt_nyelv = nyelvek.pop()
print(f'Törölt nyelv {torolt_nyelv}')
nyelvek.pop(1)

# eltávolítja a megadott indexű elemet
del nyelvek[1]
print(nyelvek)
# eltávolítja a megadott elemet az elsőként megtalált pozícióból
nyelvek.remove('Python')
print(nyelvek)
# törli a listát
nyelvek.clear()
print(nyelvek)  