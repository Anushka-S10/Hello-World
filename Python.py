# if - else
user_names = ['admin','eric','george','jack']
for user_name in user_names:
	if user_name=="admin":
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello" + user_name.title() + " ,thank youfor logging in again.")

# dictionary
info = { 'name':'william','age':22,'city':'Los Angles'}
print(info)

# looping in dictonary
state_capitals = {'bihar':'patna','tamilnadu':'chennai','karnataka':'banglore','uttar pradesh':'lucknow'}
print("The following capitals has been mentioned:")
for capital in state_capitals.values():
	print(capital.title())

# while loop
x = 1
while x < 10:
	print(x)
	x += 1

birds = ['parrot','peacock','hen','pigeon','duck','hen']
print(birds)
while 'hen' in birds:
	birds.remove('hen')
	print(birds)

# import module
from math import*
print(pi)
print(factorial(6))

# classes
class Bike():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
	def get_descriptive_name(self):
		long_name = str(self.year)+'  '+self.make+'  '+self.model
		return long_name.title()
my_new_bike = Bike('KTM', 'a5', 2018)
print(my_new_bike.get_descriptive_name())