def volMasseEllipsoide(a = 1, b = 1, c = 1, rho = 1):
    v = (4 / 3) * math.pi * a * b * c
    m = v * rho
    return (v, m)

print(volMasseEllipsoide())
print(volMasseEllipsoide(2, 3, 4, 5))
