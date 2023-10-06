# Dictionary.
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
         }

cities = {
    'CA': 'San Francisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
    }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 11)
print("Michigan's abbrevation is: ", states['Michigan'])
print("Florida abbrevation is: ", states['Florida'])

print('-' * 11)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 11)
for abbrev, city in list(cities.items()):
    print(f"{states} is abbreviated {abbrev}")

print('-' * 11) 
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has a city {city}")

print('-' * 11) 
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 11) 
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is {city}")
