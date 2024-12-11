first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and third == second:
    print(3)
elif len({first,second,third}) < 3:
    print(2)
else:
    print(0)
