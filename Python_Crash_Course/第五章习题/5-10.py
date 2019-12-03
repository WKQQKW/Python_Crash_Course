#检查用户名
current_users = ['MASK', 'tom', 'jerry', 'admin', 'jesh']
new_users = ['Mask', 'tom', 'jerr', 'admi', 'jes']
current_users_lower = []
for user in current_users:
    user = user.lower()
    current_users_lower.append(user)
for user in new_users:
    if user.lower() in current_users_lower:
        print('You should input another name!')
    else:
        print('User name not be used!')