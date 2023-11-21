import math

flottant = float(input("Entrez un flottant: "))
if flottant >= 0:
    racine = math.sqrt(flottant)
    print(f"La racine de {flottant} est {racine}.")
else:
    print("Erreur: le flottant doit être positif ou nul.")

mot1 = input("Entrez le premier mot: ")
mot2 = input("Entrez le deuxième mot: ")
if mot1 < mot2:
    print(f"Le mot {mot1} est plus petit que le mot {mot2}.")
elif mot1 > mot2:
    print(f"Le mot {mot2} est plus petit que le mot {mot1}.")
else:
    print(f"Les mots {mot1} et {mot2} sont égaux.")

print(f"Le mot {mot1} est plus petit que le mot {mot2}." if mot1 < mot2 else f"Le mot {mot2} est plus petit que le mot {mot1}." if mot1 > mot2 else f"Les mots {mot1} et {mot2} sont égaux.")

pSeuil = 2.3
vSeuil = 7.41
pression = float(input("Entrez la pression de l'enceinte: "))
volume = float(input("Entrez le volume de l'enceinte: "))
if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat.")
elif pression > pSeuil:
    print("Augmentez le volume de l'enceinte.")
elif volume > vSeuil:
    print("Diminuez le volume de l'enceinte.")
else:
    print("Tout va bien.")
