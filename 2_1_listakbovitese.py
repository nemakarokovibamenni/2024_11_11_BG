nyelvek = ['Python', 'C', 'C++', 'Java', 'Python']

# a lista végére hozzáfűz egy elemet
nyelvek.append('Python')
print(nyelvek)

# a listát másolja
nyelvek_masolat = nyelvek.copy()
print(nyelvek)

# a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)

# adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')  
print(nyelvek)
len(nyelvek)
print(len(nyelvek))