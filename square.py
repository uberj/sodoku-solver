from collections import namedtuple
Square = namedtuple('Square', ['coordinate', 'choice', 'choices'])
class Square(object):
    # NOTE, no internet so no attr library
    coordinate = None
    choice = None
    choices = None
    def __init__(self, coordinate, choice, choices):
        self.coordinate = coordinate 
        self.choice = choice 
        self.choices = choices 

    def __repr__(self):
        return '<Square: %s>' % self

    def __str__(self):
        return 'coordinate:%s choice:%s choices:%s' % (
                self.coordinate, self.choice, self.choices)

