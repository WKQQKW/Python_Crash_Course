#宠物
dog = {'type': 'mammal', 'owner': 'Jack'}
cat = {'type': 'mammal', 'owner': 'Tom'}
pig = {'type': 'mammal', 'owner': 'Lucy'}
pets = [dog, cat, pig]
print(pets)
for pet in pets:
    for key, value in pet.items():
        print('\n' + key + ':' + value)
