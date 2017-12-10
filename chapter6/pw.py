#! python3

# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'sdgsagF3teY5YDSF',
             'blog': 'sdf934thj9sdh935dcx',
             'lugage': '13345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       # first command line arg in the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for %s copied to clipboard.' % (account))
else:
    print('There is no account named ' + account)


    
