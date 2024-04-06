# encoding=utf-8
'''
# ch02: Python variables and data types
message = 'Hello, Python!'
print(message)
message = 'Hello, Python Crash Course world!'
print(message)
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

favarite_language = ' python '
print(favarite_language.rstrip())
print(favarite_language.lstrip())
print(favarite_language.strip())

# ex02-03
name = 'Eric'
message = 'Hello ' + name + ', would you like to learn some Python today?'
print(message)

import this
'''

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!

# ch03: Introducing Lists
'''
names = ['Michael', 'Bob', 'Tracy']
# excercise 3-1
print(names)
# excercise 3-2
for name in names:
    print(f'Hello, {name}!')
# excercise 3-3
transportations = ['car', 'bicycle', 'motorcycle']
for transportation in transportations:
    print(f'I would like to own a {transportation}.')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(0, 'bmw')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive.title()} is too expensive for me.')

# excercise 3-4
guests = ['Alice', 'Bob', 'Cathy']
for guest in guests:
    print(f'Hello, {guest}! Would you like to have dinner with me?')
# excercise 3-5
print(f'\n{guests[1]} can\'t make it.')
guests[1] = 'David'
for guest in guests:
    print(f'Hello, {guest}! Would you like to have dinner with me?')
# excercise 3-6
print('\nI found a bigger table.')
guests.insert(0, 'Eve')
guests.insert(2, 'Frank')
guests.append('Grace')
for guest in guests:
    print(f'Hello, {guest}! Would you like to have dinner with me?')    
# excercise 3-7
print('\nI can only invite two guests.')
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f'Sorry, {popped_guest}.')
for guest in guests:
    print(f'Hello, {guest}! Would you like to have dinner with me?')
del guests[0]
del guests[0]
print(guests)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nHere is the original list:{cars}')
cars.sort()
print(f'\nHere is the sorted list:{cars}')
cars.sort(reverse=True)
print(f'\nHere is the sorted list in reverse order:{cars}')
new_cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'\nHere is sorted list:{sorted(new_cars)}')
print(f'\nHere is inverse sorted list:{sorted(new_cars, reverse=True)}')
new_cars.reverse()
print(f'\nHere is the original list in reverse order:{cars}')
new_cars.reverse()
print(f'\nHere is the original list again:{cars}')
# excercise 3-8
places = ['monaco', 'tokyo', 'new york', 'london', 'paris']
print(places)
print(sorted(places))
print(places)
print(places.reverse())
print(places.reverse())
print(sorted(places))
print(sorted(places, reverse=True))
'''

# ch4: Working with Lists
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
num_generater = range(1, 6)
print(f'numbers:{numbers}')
print(f'num_generater:{num_generater}')
for value in num_generater:
    print(value)

even_numbers = list(range(2, 11, 2))
odd_numbers = list(range(1, 10, 2))
print(f'even_numbers:{even_numbers}')
print(f'odd_numbers:{odd_numbers}')
print('squares v1:')
print([value*value for value in range(1, 11)])
print('squares v2:')
print([value**2 for value in range(1, 11)])
print('squares v3:')
print(value**2 for value in range(1, 11))

# excercise 4-3
exc_numbers = list(range(1, 21))
for number in exc_numbers:
    print(number)
# excercise 4-4
large_numbers = list(range(1, 1000001))
for number in large_numbers:
    print(number)
# excercise 4-5
print(f'min:{min(large_numbers)}')
print(f'max:{max(large_numbers)}')
print(f'sum:{sum(large_numbers)}')
# excercise 4-6
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
# excercise 4-7
multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)
# excercise 4-8
cubes = [value**3 for value in range(1, 11)]
print(f'The first three items in the list are:{cubes[:-1]}')
# excercise 4-9
first_ten_cubes = [value**3 for value in range(1, 11)]
for cube in first_ten_cubes:
    print(cube)
