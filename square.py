from collections import namedtuple

class Square(object):
    # NOTE, no internet so no attr library
    coordinate = None
    choice = None
    mutable = True
    def __init__(self, coordinate, choice, mutable=True):
        self.coordinate = coordinate 
        self.choice = choice 
        self.mutable = mutable

    def __repr__(self):
        return '<Square: %s>' % self

    def __str__(self):
        return 'coordinate:%s choice:%s' % (self.coordinate, self.choice)

