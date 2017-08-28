from collections import namedtuple
Square = namedtuple('Square', ['coordinate', 'choice', 'choices'])
class Square(object):
    # NOTE, no internet so no attr library
    coordinate = None
    choice = None
    def __init__(self, coordinate, choice):
        self.coordinate = coordinate 
        self.choice = choice 

    def __repr__(self):
        return '<Square: %s>' % self

    def __str__(self):
        return 'coordinate:%s choice:%s' % (self.coordinate, self.choice)

