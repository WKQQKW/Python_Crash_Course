#以特殊的方式和管理员打招呼
names = ['mask', 'tom', 'jerry', 'admin', 'jesh']
for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + name + ' thank you for logging in again.')