#添加嘉宾
names = ['Tom', 'Jerry', 'Jack', 'Kobe', 'James']
for name in names:
    if name == 'Jack':
        print(name + ' enable not to participate in dinner')
        names.append('Rose')
        names.remove('Jack')
names.insert(0, 'Harden')
names.insert(3, 'Bob')
names.append('Thomas')
print('I would like to invite ' + ', '.join(names) + ' to have dinner.')
print('I have find a bigger table')