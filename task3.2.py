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