# Dictionaries
cat = {'size':'fat','color':'white'}
cat['size']
'My cat has ' + cat['color'] + ' fur.'
dog = {'color':'white'}
cat == dog
list(cat.keys())                   # For keys in dictionary
list(cat.values())                 # For values in dictionary
list(cat.items())                  # for showing the lists in dictionary
cat.keys()
cat.setdefault('age',8)

for k in cat.keys():
     print(k)

# Count the characters
msg = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in msg.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1
print(count)

import pprint          # To print it in vertical order
msg = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in msg.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1
pprint.pprint(count)


#This is a guess the number game

import random
print('Hello, what is your name?')
name = input()
secretNumber = random.randint(1,20)
print('Well, '+name+',I am thinking of a number between 1 and 20')
#print('DEBUG: Secret number is '+str(secretNumber))
for guessesTaken in range(1,7):
      print('Take a guess')
      guess = int(input())
      if guess < secretNumber:
          print('Your guess is too  low.')
      elif guess > secretNumber:
          print('Your guess is too high.')
      else:
          break
if guess == secretNumber:
      print('Good job, '+name+'! You guessed my number in '+str(guessesTaken)+' guesses.')
else:
      print('Nope. The number I was thinking of was '+ str(secretNumber))
      

