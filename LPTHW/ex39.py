# Dictionaries

'''
Chung ta da hoc list
	things = ['a', 'b', 'c', 'd']
	things[1] = b
	things[2] = c

Chung ta co the su dung "index" cho list. Va chung ta chi co the dung so de tim
ra phan tu cua mot danh sach.

Tuy nhien mot dictianary cho phep ban su dung nhieu thu, khong chi la so. Hay xem

	stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
	print stuff['name']
	Zed
	print stuff['age']
	36
	print stuff['height']
	74
	stuff['city'] = "San Francisco"
	print stuff['city']
	Franci

Thay vi dung chi so, chung ta su dung chuoi (ten) de trich phan tu trong mot tu dien
Chung ta cung co the them nhung phan tu moi bang cach nhu tren.
Chung ta cung co the lam nhu sau:

	stuff[1] = "Wow"
	stuff[2] = "Neato"
	print stuff[1]
	Wow
	print stuff[2]
	Neato
	print stuff
	{'city': 'San Francisco', 2: 'Neato', 'name': 'Zed', 1: 'Wow', 
	'age': 36, 'height': 74}

Ban cung co the xoa cac phan tu trong 1 dict:
	del stuff['city']
	del stuff[1]
	del stuff[2]
	stuff
	{'name': 'Zed', 'age': 36, 'height': 74}

'''

# Create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# Create a basic set pf states and some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# and some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '_' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '_' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '_' * 10
print 'Michigan has: ', cities[states['Michigan']]
print 'Florida has: ', cities[states['Florida']]

# print every state abbreviation
# Phuong thuc items() tra ve tat ca cac cap (key-value) cua mot dict
print '_' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '_' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# no do both at the same time
print '_' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(
		state, abbrev, cities[abbrev])


# phuong thuc dict.get(Key, value) tra ve gia tri cua Key da cho, neu key khong
# co mat trong dict thi phuong thuc nay tra ve gia tri None
print '_' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

# get a city with a default values
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city