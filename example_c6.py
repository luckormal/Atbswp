'''while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    password = input('Select a new password (letters and numbers): ')
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
                
'''

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth, '0'))

picnicItems = {'sandwiches': 4, 'apples':12, 'cups': 4, 'cookies':8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
