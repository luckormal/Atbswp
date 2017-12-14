
import re
'''
heroRegex = re.compile(r'Bat(wo)?man')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1)

'''
'''
haRegex = re.compile(r'(Ha){3,5}?')
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())
'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 456-555-9999 Work: 215-555-0000')
print(mo)
