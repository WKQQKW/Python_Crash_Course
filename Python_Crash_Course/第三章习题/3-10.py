#尝试使用各个函数
cities = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'zhuhai']
print(cities[0])
print(cities[0].title())
print(cities[-1])
for city in cities:
    print('I Love ' + city.title())
cities[0] = 'bayuquan'
print(cities)
cities.append('beijing')
print(cities)
cities.insert(0, 'tianjin')
print(cities)
del cities[0]
print(cities)
cities.pop()
print(cities)
cities.remove('zhuhai')
print(cities)
cities.sort()
print(cities)
cities.reverse()
print(cities)
print(len(cities))