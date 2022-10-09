# Managing complex Regex

import re
#verbose mode - ignore whitespace  and commetns inside regular ecpression 

comRegex = re.compile(r'''(
(\d{3}|\(d{3}\))?            # area code
(\s|-|\.)?                   # seperator
\d{3}                        # First 3 Digit    
(\s|-|\.)?                   # Seperator
\d{4}                        # last four digit
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''',re.VERBOSE|re.I | re.DOTALL)

mo1 = comRegex.search('but check out the resources at http://nostarch.com/automatestuff/ for more information.')
print(mo1.group())