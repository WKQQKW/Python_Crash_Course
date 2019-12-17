#喜欢的地方
favorite_places = {'Tom': ['Beijing', 'shanghai', 'guangzhou'],
                   'Jack': ['shenyang', 'haerbin', 'jilin'],
                   'Loyer': ['aomen', 'zhuhai', 'foshan']}
for name, places in favorite_places.items():
    print('\n' + name + ' favorite places: ')
    for place in places:
        print('\t' + place)