
import re
'''
heroRegex = re.compile(r'Bat(wo)?man')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1)


haRegex = re.compile(r'(Ha){3,5}?')
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 456-555-9999 Work: 215-555-0000')
print(mo)


xmasRegex = re.compile(r'\d+\s\w+')
xmas = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
                 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves,  \
                 1 partridge')
print(xmas)

vowelRegex = re.compile(r'[^a-ceiouAEIOU]')
vow = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vow)
'''

namesRegex = re.compile(r'Agent (\w)\w*')
name = namesRegex.sub(r'\1*****', 'Agent Alice gave the secret documents to Agent Bob.')
print(name)
