#/usr/bin/python

import collections
 
def build(CNF):
    G = collections.defaultdict(list)
    for left, right in CNF:
        G[right].append(left)
    return G
 
def cky(G, W):
    T = [[[] for j in range(len(W)+1)] for i in range(len(W))]
    for j in range(1, len(W)+1):
        T[j-1][j] += G.get(W[j-1], [])
        print "[%d,%d]: %r" % (j-1, j, G.get(W[j-1]))
        for i in range(j-2, -1, -1):
            for k in range(i+1, j):
                for x in T[i][k]:
                    for y in T[k][j]:
                        T[i][j] += G.get((x,y), [])
                        print "[%d,%d]: %r (%s [%d,%d] and %s [%d,%d])" % (
                            i,j,G.get((x,y)),x,i,k,y,k,j)
    return T
 
if __name__ == '__main__':
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
    G = build(CNF)
    T = cky(G, ('time', 'flies', 'like', 'an', 'arrow'))
