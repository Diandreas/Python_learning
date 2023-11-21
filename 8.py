import math

for x in range(-3, 4):
    try:
        y = math.sin(x) / x
        print(y)
    except ZeroDivisionError:
        print("Division par zéro.")
