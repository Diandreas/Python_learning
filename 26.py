p = int(input("Entrez un nombre entier P: ")) # Nombre P
q = int(input("Entrez un nombre entier Q: ")) # Nombre Q
if p % q == 0: # Si Q divise P
    print(f"Le nombre Q={q} divise le nombre P={p}.")
else: # Sinon
    print(f"Le nombre Q={q} ne divise pas le nombre P={p}.")
