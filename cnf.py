#/usr/bin/python

import collections

class CNF:
    def __init__(self,Grammar,keys):
        G = collections.defaultdict([])
        keys = Set([])
    description = "Chomsky Normal Form Grammar"
    author = "Team Hom/Waltner"

    def insertGrammar(self, listo):
        i = 0
        for e in listo:
            if i == 0:
                keys.add[i]
            else:
                pass

 
 
if __name__ == '__main__':

    """
    CNF = (
        ('S', ('NP','VP')),
        ('S', ('VP','NP')),
        ('VP', 'time'),
        ('VP', 'flies'),
        ('VP', 'like'),
        ('VP', 'arrow'),
        ('VP', ('Verb','NP')),
        ('VP', ('VP','PP')),
        ('NP', 'time'),
        ('NP', 'flies'),
        ('NP', 'arrow'),
        ('NP', ('Det','NP')),
        ('NP', ('Noun','NP')),
        ('NP', ('NP','PP')),
        ('PP', ('Preposition','NP')),
        ('Noun', 'time'),
        ('Noun', 'flies'),
        ('Noun', 'arrow'),
        ('Verb', 'time'),
        ('Verb', 'flies'),
        ('Verb', 'like'),
        ('Verb', 'arrow'),
        ('Preposition', 'like'),
        ('Det', 'an'),
    )
    """
