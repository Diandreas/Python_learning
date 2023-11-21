def cube(x):
    return x ** 3

def volumeSphere(r):
    return (4 / 3) * math.pi * cube(r)

print(volumeSphere(2))
