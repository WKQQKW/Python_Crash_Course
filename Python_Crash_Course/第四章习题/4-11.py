#你的披萨和我的披萨
pizzas = ['水果披萨', '黑椒披萨', '蛋黄披萨']
friend_pizzas = pizzas[:]
pizzas.append('榴莲披萨')
friend_pizzas.append('火腿披萨')
for pizza in pizzas:
    print(pizza)
print('\n')
for pizza in friend_pizzas:
    print(pizza)