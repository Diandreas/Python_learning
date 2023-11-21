import easygui

truc = []
machin = [0.0] * 5
easygui.msgbox(f"truc = {truc}, machin = {machin}")

for i in range(4):
    print(i)

for i in range(4, 8):
    print(i)

for i in range(2, 9, 2):
    print(i)

chose = list(range(6))
print(3 in chose)
print(6 in chose)
