red = []
blue = []

for i in range(1,7):
    red.append(f'red {i}')
    blue.append(f'blue {i}')

print(red)
print(blue)
print("-------------------------------")

combo = []
for die in red:
    for dice in blue:
        combo.append((die, dice))

print(combo)
print("-------------------------------")

red = [f'red {i}' for i in range(1,7)]
print(red)

red = [f'blue {i}' for i in range(1,7)]
print(blue)
print("-------------------------------")

combo = [(r_die, b_die) for r_die in red   for b_die in blue]
print(combo)
