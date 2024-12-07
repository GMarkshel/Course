# 1st
my_dict = {'Galina': 2001, 'Artem': 2010, 'Maria': 1998 }
print('Dict: ',my_dict)
print('Existing value: ', my_dict['Artem'])
print ('Not existing value: ', my_dict.get('Daria'))
my_dict.update({'Alex': 1994, 'Emily': 1999})
delete_date = my_dict.pop ('Maria')
print ('Deleted value: ', delete_date)
print('Modified dictionary: ',my_dict)

# 2nd
my_set = {0.248, 13, 'People', False,('day', 'night'), 0.248, 13, True, 13, 'People', }
print('Set: ', my_set)
my_set.update(['Human',7])
my_set.remove(('day', 'night'))
print('Modified set: ', my_set)
