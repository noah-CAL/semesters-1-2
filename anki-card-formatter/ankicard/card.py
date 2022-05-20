"""Contains the definition of the Card() class that contains fields for cloze, explanation, etc."""

class Card():
    def __init__(self, fields: dict, tags: str) -> None:
        """
        #TODO Redo this docstring
        All arguments (except for card_type) are optional, and correspond to the fields listed in Card.FIELDS .
        Only the necessary fields will be used to create the card specified in card_type
        :param str card_type: structure of the card to create (e.g. 'code' 'math' etc..)
        """
        if type(tags) != str:
            raise Exception('tags parameter must be a string!')

        self.fields = fields
        self.tags = tags
    
    """Instance methods"""
    def get_fields(self) -> None:
        """Prints all the fields in a nice visual format"""
        for field in self.fields:
            print(f'{field}: {self.fields[field]}')

    def __str__(self, delimeter='\t') -> str:
        """
        Returns textual representation of a card separated by a delimeter that can be imported into Anki
        :param str delimeter: delimeter to separate the fields -- default is the tab character \t
        """
        res = ''
        for val in self.fields.values():
            res += val + delimeter

        res += self.tags
        return res


    """Class methods"""
    @staticmethod
    def output_to_text(cards: list):
        """
        Takes a list of Card objects and output to output.txt
        :param List<Card> cards: list of Card objects 
        """
        with open('output.txt', 'w') as f:
            for card in cards:
                f.write(str(card) + '\n')
        print('Outputted cards to output.txt')