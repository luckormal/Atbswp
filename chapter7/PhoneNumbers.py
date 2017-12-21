#! python3
# phoneNumber.py - Find phone numbers and email addresses on the clipboard.

import re, pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      #area code
    (\s|-|





    )''', re.VERBOSE)
