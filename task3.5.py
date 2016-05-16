
def LEFT(string, index):#MAKING IT INTO A FUNCTION
	return string[0:index]

nf = open('membersinfo.txt', 'w') #nf=new file
f = open('club', 'r')
for line in f:
	print (line)
	line = LEFT(line, len(line)-1)
	phone = raw_input('Enter telephone number: ')
	date = raw_input('Enter membership data: ')
	print('\n')
	nf.write(line+',' + phone + ',' + date + '\n')
nf.close()
f.close()

