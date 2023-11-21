def table(base, debut, fin, inc):
    for i in range(debut, fin + 1, inc):
        print(f"{base} x {i} = {base * i}")

table(2, 1, 10, 1)
