immutable_var = (1, 'Sun', False, 6.5, ['capricorn', 'leo', 'scorpio'] )
print(immutable_var)
# immutable_var [0] = 2 - - ошибка
# immutable_var [1] = 'Moon' - ошибка
immutable_var [4][1] = 'aquarius'
print(immutable_var)
# функция tuple не поддерживает изменение объектов,  так как является ссылкой на список,а не самим списком
# Но можно изменять непосредственно в самом элементе, если, например, это список
mutable_list = [13,'Python',True,7,'Course']
mutable_list [2] = 13.95
mutable_list [4] = 'Urban'
print(mutable_list)
