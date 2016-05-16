def ValidateUserID():
	if len(UserID) != 6:
		print ('Invalid. Please enter only 6 characters.')
	elif ((ord(UserID[0])<= ord('Z') and ord(UserID[0])>=ord('A')) 
	and (ord(UserID[1])<= ord(('z')) and ord(UserID[1])>=ord('a')) 
	and (ord(UserID[2])<= ord('z') and ord(UserID[2])>=ord('a')) 
and (UserID[3:6].isdigit())):
		print ('Correct Format. Member validation successful.')
		return True
	else:
		print ('Wrong Format. Please try again later.') 
		return False

f = open('club', 'w')
for i in range(3): ### 3 = number of entries we are taking.
### there's nothing specified in the question so we go with 3 for our ease

	name = raw_input('Enter member name: ')
	UserID = raw_input('Enter member id: ')
	Validation = ValidateUserID()
	if Validation == True:
		f.write(name+ ',' + UserID + '\n')

f.close()

### Printing contents of file
f = open('club', 'r')
print('\n\n***MEMBER NAMES AND MEMBER IDs***\n')
for line in f:
	print (line + '\n')
f.close()