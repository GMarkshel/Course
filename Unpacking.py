def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

    # 1. Функция с параметрами по умолчанию:
print_params(('one', 'two'))
print_params({'key_1': 3, 'key_2': 4},False)
print_params(1,[3.7,6,1], 'string')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

    # 2. Распаковка параметров:
values_list = ['word', {'name': 'Anna', 'age': 27}, 13]
values_dict = {'a': 'string', 'b': (13,4), 'c': 5.9}
print_params(*values_list)
print_params(**values_dict)

    # 3. Распаковка + отдельные параметры:
values_list_2 = ['list', False]
print_params(*values_list_2, 42)
