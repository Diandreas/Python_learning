tva = 0.2 # Taux de TVA
ttc = float(input("Entrez un montant TTC: ")) # Montant TTC
ht = ttc / (1 + tva) # Montant HT
print(f"Le montant HT correspondant est {ht}.")
