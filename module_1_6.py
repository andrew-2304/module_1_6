my_dict = {'Andrey': 2000, 'Svetlana': 1973}
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Elena'))
my_dict.update({'Alexey': 2009,
                'Alexander': 2006})
a = my_dict.pop('Svetlana')
print(a)
print(my_dict)
my_set = {'Andrey', 2, 8, 3, 2, 1, 3, True, (1, 2, 3)}
print(my_set)
my_set.update([0, 9])
my_set.remove('Andrey')
print(my_set)