import random

num = [numbers for numbers in range(3,21)]
a = random.choice(num)
#print(a)
d = ''

for b in range(1, a):
    for c in range(b,a):
        if a % (c + b) == 0:
            if c == b:
                continue
            else:
                d = d + str(b) + ',' + str(c) + ' '
print(f'Cлучайное число: {a}, Пароль: {d}')
