nombre = int(input("Entrez un nombre entier: ")) # Nombre
print(f"Les diviseurs de {nombre} sont:")
for i in range(1, nombre + 1): # Pour i allant de 1 à nombre
    if nombre % i == 0: # Si i est un diviseur de nombre
        print(i) # Affichage de i
