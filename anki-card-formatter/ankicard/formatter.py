"""
Defines format() function to format code into HTML tags to be read by Anki in combination w/ CSS selectors
"""
from pygments import highlight
from pygments.formatters import HtmlFormatter

# import lexers for each language
from pygments.lexers import PythonLexer
from pygments.lexers.javascript import JavascriptLexer
from pygments.lexers.html import HtmlLexer
from pygments.lexers.shell import BashLexer
from pygments.lexers.sql import MySqlLexer
from pygments.lexers.lisp import SchemeLexer

def format(code: str, lang: str ) -> str: 
    """
    Takes input code and returns a string of HTML with approriate <div> / <span> classes
    :param str code: code to format
    :param str lang: OPTIONAL parameter to specify language - default is 'python', options are currently: 'python' 'javascript' 'bash' 'html'
    """
    lexers = {
        'python': PythonLexer,
        'javascript': JavascriptLexer,
        'bash': BashLexer,
        'html': HtmlLexer,
        'sql': MySqlLexer,
        'scheme': SchemeLexer,
        # etc...
    }
    lexer = lexers[lang]
    formatted = highlight(code, lexer(), HtmlFormatter())

    # add language class to container div
    div = f'<div class="highlight {lang}">'
    return formatted.replace('<div class="highlight">', div)

# TEST
# if __name__ == '__main__':
#     print(format("""def func(a, b) -> None:
#         return a + b""", 'javascript'))

def format_file(file: str):
    with open('output.txt', 'w') as out:
        with open(file, 'r') as f:
            for line in f:
                out.write(format(line, 'python'))