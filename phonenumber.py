import re

somestr = 'Just some string, here\'s a phone number 834-355-924, another 982-023-423 and 843-334-244'

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{3}') # looks for 3 digits, each 3 separated with '-' symbol - finds only 1 number, use findall() to find all numbers

match_object = phoneNumRegex.search(somestr)
mo2 = phoneNumRegex.findall(somestr) # returns a list

print('Looking for RE using \'search\' : '  + match_object.group())
print('Looking for RE using \'findall\' : '  + str(mo2))
