
vhod = int(input())

bonus = 0.0
if vhod <= 100:
    bonus = 5
elif vhod > 100 or vhod < 1000:
    bonus = vhod * 0.2
else:
    bonus = vhod * 0.1

if vhod % 2 == 0:
    bonus = bonus + 1
if vhod % 5 == 0:
    bonus = bonus + 2

print(bonus)
print(bonus+vhod)