def password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                pairs.append(f'{i}{j}')
    result = ''.join(pairs)
    return result

while True:
    n = int(input('Введите число от 3 до 20: '))
    if 3 <= n <= 20:
        print(password(n))
        break
    else:
        print('''Число должно быть от 3 до 20
                                            ''')
