entier = int(input("Entrez un entier entre 1 et 10: "))
while entier < 1 or entier > 10:
    print("Erreur: l'entier doit être entre 1 et 10.")
    entier = int(input("Entrez un entier entre 1 et 10: "))
print(f"Vous avez saisi {entier}.")
