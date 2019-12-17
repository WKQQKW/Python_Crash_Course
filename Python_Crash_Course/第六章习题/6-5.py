#河流
river = {'nile': 'eqypt', 'Danube': 'Austria', 'Amazon River': 'Peru'}
for key, value in river.items():
    print('The ' + value + 'runs through ' + key)
print()
for value in river.values():
    print(value)
print()
for key in river.keys():
    print(key)