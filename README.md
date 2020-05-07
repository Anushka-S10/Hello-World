# Hello-World
#Lists
guests= ['Percy','Nalini','Sneha','Swati']
del guests[2] #deletion
guests.append('Snigdha') #insertion
print(guests)
print(len(guests)) #for length
guests.insert(1,'Aish')
print(guests)
popped_guest = guests.pop() #removal of guests
popped_guest = guests.pop()
print(guests)
print(sorted(guests)) # in sorted order
print(guests[-1])
for guest in guests:
	print(guest.title()+", you are invited to attend the party.\n")
print("Thanks for coming.")
