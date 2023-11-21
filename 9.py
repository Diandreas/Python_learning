import easygui

liste = [1, 2, 3, 4, 5]
entier = easygui.integerbox("Entrez un entier: ")
for element in liste:
    if element == entier:
        easygui.msgbox(f"L'entier {entier} est dans la liste.")
        break
else:
    easygui.msgbox(f"L'entier {entier} n'est pas dans la liste.")

entier = easygui.integerbox("Entrez un entier positif: ")
diviseur = 2
while diviseur < entier:
    if entier % diviseur == 0:
        easygui.msgbox(f"L'entier {entier} n'est pas premier, il est divisible par {diviseur}.")
        break
    diviseur = diviseur + 1
else:
    easygui.msgbox(f"L'entier {entier} est premier.")
