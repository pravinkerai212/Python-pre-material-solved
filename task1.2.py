#Task1.2
input1 = raw_input('Enter First Name: ')
input2 = raw_input('Enter Second Name: ')

name = 'First Name: ' + input1 + ', ' + 'Last Name: ' + input2

a = name.find(':')
b = name.find(',')
c = name.find('Last')

firstname = name[a+2:b]
lastname = name[c+11:len(name)]

print firstname, lastname
print name[a+2], lastname
print lastname + ', ', firstname
print 'Mr', name[a+2], lastname
print 'Dear Mr', firstname 
print name
print firstname, lastname.upper()

# Enter First Name: Pravin
# Enter Second Name: Kalyan
# Pravin Kalyan
# P Kalyan
# Kalyan,  Pravin
# Mr P Kalyan
# Dear Mr Pravin
# First Name: Pravin, Last Name: Kalyan
# Pravin KALYAN