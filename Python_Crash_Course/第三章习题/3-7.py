#缩减名单
names = ['Tom', 'Jerry', 'Jack', 'Kobe', 'James']
print('Sorry, because the table enable not to instantly arrive. I can only invite two pepole.')
while len(names) > 2:
    names.pop()
for name in names:
    print(name + ', you still can participate in the dinner.')
while len(names) != 0:
    del names[len(names) - 1]
print(names)