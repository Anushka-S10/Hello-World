# Files
file_path = 'msgs.txt'  #(your file_path name)
with open(file_path,'w') as f:
	f.write("I love programning.\n")
	f.write("I love to code.\n")
	
# to append a file
file_path = 'msgs.txt'
with open(file_path,'a') as f:
	f.write("I love to explore things\n")

# guest list
name = input("Name:")
filename = 'msgs.txt'
print("enter 'q' when you are finished.")
while True:
	name = input("\n Name:")
	if name == 'q':
		break
	else:
		with open(filename,'a') as f:
			f.write(name+"\n")
		print("Hi " +name+", you have been invited in function.")

# Exceptions
try:
	print(5/0)
except ZeroDivisionError:
	print("It's an error. It is not divisible by zero.")

# FileNotFoundError Exception
def count_words(filename):
	try:
		with open(filename) as f:
			contents = f.read()
	except:
		msg = "Sorry, the file"+filename+"does not exist"
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file" + filename + "has about" + str(num_words)+ "words.")
filenames = ['sleeping_beauty.txt','cindrella.txt','snow_princess.txt']
for filename in filenames:
	count_words(filename)