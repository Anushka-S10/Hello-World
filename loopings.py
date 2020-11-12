#Numerical lists 
for values in range(1,14): 
    print(values) 
    value = list(range(1,10)) 
    print(sum(value)) 
    print(max(value)) 
    print(min(value)) 
    odd = list(range(1,11,2)) 
    print(odd) 

#List Comprehensions 
squares = [value**2 for value in range(1,11)] 
print(squares) 
multiple = [value*3 for value in range(1,10)] 
print(multiple) 
countries = ['France','Japan','London','Italy','Singapore','Switzerland'] 
print(countries[0:3]) 
print(countries[2:]) 

#loop in lists 
print("Here is the name of countries") 
for country in countries: 
    print(country.title()) 

#Looping in tuple 
dimensions = (400,200) 
for dimension in dimensions: 
    print(dimension)