"""Main script to mass-generate cards"""
from ankicard.card import Card
from ankicard.fields import math_field
from ankicard.formatter import format

cards = []

def mass_create_math(clozes:list, titles:list, explanation, image, source, tags):
    for i, cloze in enumerate(clozes):
        title = titles[i]

        fields = math_field(cloze=cloze, title=title, explanation=explanation, image=image,  source=source)
        card = Card(fields, tags=tags)
        cards.append(card)

mass_create_math(
    [
        
    ], #clozes
    [

    ], #titles
    r'', #explanation
    '', #image
    '', #source
    '' #tags
)

Card.output_to_text(cards)