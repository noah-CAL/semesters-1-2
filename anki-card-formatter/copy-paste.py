import pyperclip
import sys
from ankicard.formatter import format

code = pyperclip.paste()
lexer = 'python'
if len(sys.argv) > 1:
    lexer = sys.argv[1]

with open('output.txt', 'w') as f:
    # f.write(format(str, 'python'))
    # try:
    formatted_code = format(code, lexer)
    print(f'Formatting with {lexer}')
    # except KeyError as e:
    #     raise('Invalid language specified: ', e)
    f.write(formatted_code)
    pyperclip.copy(formatted_code)
    print(f'outputted to {f} and copied to clipboard!')
