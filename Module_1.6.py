my_dict = {'Motya': 1965, 'Dasha': 1995, }
print(my_dict)
print(my_dict.get('Motya'))
print(my_dict.get('Ivan', 'без ошибки'))
my_dict.update({'Ivan': 1991,
                'Vova': 1984})
my_dict_1 = my_dict.pop('Dasha')
print(my_dict)

# print(my_dict.values())
# print(my_dict_1)
