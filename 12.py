def maFonction(x):
    return 2 * x ** 3 + x - 5

def tabuler(fonction, borneInf, borneSup, nbPas):
    pas = (borneSup - borneInf) / nbPas
    x = borneInf
    while x <= borneSup:
        print(f"f({x}) = {fonction(x)}")
        x = x + pas

tabuler(maFonction, 0, 10, 10)
