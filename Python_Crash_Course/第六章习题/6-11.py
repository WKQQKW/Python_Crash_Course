#城市
cities = {'北京': {'country': '中国', 'population': '2154.00万人', 'fact': '首都'},
          '沈阳': {'ciuntry': '中国', 'population': '831.6万人', 'fact': '省会'},
          '上海': {'country': '中国', 'population': '2424.00万人', 'fact': '直辖市'}}
for city, info in cities.items():
    print('\n' + city)
    for key, value in info.items():
        print('\n' + key + ':' + value)
