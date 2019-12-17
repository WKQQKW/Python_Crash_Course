#喜欢的数字
names = {'Tom': [5, 10, 15],
        'Ford': [6, 12, 18],
        'Jack': [7, 14, 21],
        'Lavin': [8, 16, 24],
        'Jerry': [9, 18, 27]}
for name, numbers in names.items():
    print('\n' + name + ' favorite nuber :')
    for number in numbers:
        print('\t' + str(number))