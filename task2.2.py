UserID = raw_input('Enter UserID: ')
if len(UserID) != 6:
	print ('Enter only 6 characters.')
elif ((ord(UserID[0])<= ord('Z') and ord(UserID[0])>=ord('A')) 
and (ord(UserID[1])<= ord(('z')) and ord(UserID[1])>=ord('a')) 
and (ord(UserID[2])<= ord('z') and ord(UserID[2])>=ord('a')) 
and (UserID[3:6].isdigit())):
	print ('Correct Format')
else:
	print ('Wrong Format') 