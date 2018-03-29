a = int(input('Первое число:'))
b = int(input('Второе:'))

while a!=0 and b!=0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(f'НОД = {a+b}')
