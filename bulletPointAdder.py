#! python3
#bulletpointAdder.py - adds wikipedia bullet points to the start
#of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

#1 paste text from th clipboard 
#2 do something to it 
#3 copy the new text to the clipboard

#TODO : separate lines and adds stars.
lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i]  #add star to each string in 'lines' list 
text = '\n'.join(lines)
pyperclip.copy(text)