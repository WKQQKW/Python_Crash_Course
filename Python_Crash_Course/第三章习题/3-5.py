#修改嘉宾名单
names = ['Tom', 'Jerry', 'Jack', 'Kobe', 'James']
for name in names:
    if name == 'Jack':
        print(name + ' enable not to participate in dinner')
        names.append('Rose')
        names.remove('Jack')
print('I would like to invite ' + ', '.join(names) + ' to have dinner.')