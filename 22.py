A = int(input("Entrez une année: "))
if (A % 4 == 0 and A % 100 != 0) or A % 400 == 0:
    print(f"L'année {A} est bissextile.")
else:
    print(f"L'année {A} n'est pas bissextile.")
