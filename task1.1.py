#Task 1.1
def left(string, index):
	return string[0 : index]

def right(string, index):
	return string[len(string) - index : len(string)]

def mid(string, index, length):
	return string[index : index + length]

#test
InputString = 'Computer Science'
print left(InputString, 4)
print mid(InputString, 4, 3)
print right(left(InputString, 6), 3)

# output
# Comp
# ute
# put