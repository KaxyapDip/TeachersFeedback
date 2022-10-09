# Wildcard character 

import re
atRegex  = re.compile(r'..at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat .')
print(mo1)


# Matching everything with Dot star 
print('''
'.' character means "Any single character except newline."
'*' character means "zero or more of the preceding character."
''')


nameRegex =  re.compile(r'First name: (.*) Last name: (.*)')
mo2 = nameRegex.search('First name: Dip Last name: Kashyap')
print(mo2.group(1))
print(mo2.group(2))
# (.*) uses greedy mode,  it will try to match as much text as possible 

nameRegex2 = re.compile(r'<.*?>')
mo3 = nameRegex2.search('<To serve man > for dinner>')
print(mo3.group())

#Matching Newlines with dot character

newLineRegex = re.compile('.*',re.DOTALL)
mo4 = newLineRegex.search('serve the public. \n Protect the innocent.')
print(mo4.group())