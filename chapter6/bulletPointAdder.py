#! python3

# bulletPointadder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
text = ''
for i in range(len(lines)):         #look through all indexes for "lines" list
    lines[i] = '* ' + lines[i]      #add star at the begining of the line

text = '\n'.join(lines)
    
    
    
    

pyperclip.copy(text)
