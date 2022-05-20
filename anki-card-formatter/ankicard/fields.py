"""Contains functions that generate specific card types that can be imported into Anki"""

def math_field(cloze: str = '', explanation: str = '', example: str = '', image: str = '', source: str = '', title: str = '') -> dict:
    """Math card template that returns a dictionary"""
    return {
        'cloze': cloze,
        'explanation': explanation,
        'example': example,
        'image': image,
        'source': source,
        'title': title,
    }

#TODO doesn't actually represent an actual code card, UPDATE THIS
def code_field(cloze: str = '', explanation: str = '', example: str = '', image: str = '', source: str = '', title: str = '') -> dict:
    """Code card template that returns a dictionary"""
    raise Exception('FIX THIS FIRST')
    return {
        'cloze': cloze,
        'explanation': explanation,
        'example': example,
        'image': image,
        'source': source,
        'title': title,
    }