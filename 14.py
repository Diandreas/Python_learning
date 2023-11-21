def somme(t):
    s = 0
    for x in t:
        s = s + x
    return s

print(somme((1, 2, 3)))
print(somme((1.5, 2.5, 3.5)))
