# case insensetive 
import re
inRegex = re.compile(r'robocop',re.I)
mo1 = inRegex.search('ROBOCop eats Baby Food')
print(mo1.group())
mo2 = inRegex.search('RoboCop eats Baby Food')
print(mo2.group())

# substituting String with sub() method 
subRegex = re.compile(r'agent \w+',re.I)
mo2 = subRegex.sub('CENSORED','Agent alice gave the secret document to agent boob')
print(mo2)

agentNameRegex = re.compile(r'agent (\w)\w*',re.I)
mo3 = agentNameRegex.sub(r'\1****','Agent alice told agent carol that agent eve knew agent bob was a double agent')
print(mo3)