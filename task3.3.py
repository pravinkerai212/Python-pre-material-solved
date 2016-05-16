def LEFT(string, index): #MAKING IT INTO A FUNCTION
	return string[0:index]
def RIGHT(string, index):
	return string[len(string)-index : len(string)]
#PRINTING THE FILE (3.2)
f = open('club','r')
data = f.readlines()
MemberName = [row[0:row.find(',')]for row in data]
MemberID = [row[row.find(',')+1:len(row)-1]for row in data]
s = '..........'
print 'MEMBER NAME: ', s, 'MEMBER ID: '
for i in range(0, len(data)):
	a = MemberName[i]
	b = MemberID[i]
	print a,'      ', s, b

f.close()

#3.3
found = False
while found == False:
	search = raw_input('\nEnter name to search: ')
	f = open('club', 'r')
	for line in f:
		id = RIGHT(line, 7)
		name = LEFT(line, line.find(','))
		if name.lower() == search.lower():
			found = True
			foundid = RIGHT(line, 7)

	if found == True:
		print (search + "'s", 'Member ID is: ' + foundid)
	else:
		print ('\nMember not found. Please enter member name again.')