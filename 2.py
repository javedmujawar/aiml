fruits = {'apple', 'banana','orange','mango'}

fruits.add("storbery")
print(fruits)

print('apple' in fruits)
print('kiwi' in fruits)

print(len(fruits))

citrus_fruits = {'orange', 'lemon','lime'}

print(citrus_fruits)

all_fruites = fruits.union(citrus_fruits)
print(all_fruites)
common_fruites = fruits.intersection(citrus_fruits)
print(common_fruites)

non_citrus_fruites = fruits.difference(citrus_fruits)
print(non_citrus_fruites)

print(fruits.issubset(all_fruites))
print(fruits.issuperset(common_fruites))

fruits.clear()
print(fruits)
