#/usr/bin/python

import collections
 
def build(CNF):
    G = collections.defaultdict(list)
    for left, right in CNF:
        G[right].append(left)
    print G
    return G
 
def cky(G, W):
    T = [[[] for j in range(len(W)+1)] for i in range(len(W))]
    for j in range(1, len(W)+1):
        T[j-1][j] += G.get(W[j-1], [])
        #print "j-1,j[%d,%d]: %s %r" % (j-1, j, W[j-1], G.get(W[j-1]))
        print "Tj-1,j [%d,%d]=%r" % (j-1,j,T[j-1][j])
        for i in range(j-2, -1, -1):
            #print "i %d" % i
            for k in range(i+1, j):
                print "k %d i %d j %d " % (k,i,j)
                for x in T[i][k]:
                    #print "Ti,k [%d,%d]=%r" % (i,k,T[i][k])
                    for y in T[k][j]:
                        #print "Tk,j [%d,%d]=%r" % (k,j,T[k][j])
                        T[i][j] += G.get((x,y), [])
                        print "i,j[%d,%d]: %r (%s [%d,%d] and %s [%d,%d])" % (
                            i,j,G.get((x,y)),x,i,k,y,k,j)
                        """
                        print i
                        print j
                        print x,y,"-->",G.get((x,y),[])
                        print x
                        print i
                        print k
                        print y
                        print k
                        print j
                        """
                        print "Ti,j[%d,%d]: %r " % (i,j,T[i][j])
    return T
 
if __name__ == '__main__':
    CNF = (
        ('S', ('NP','VP')),
        ('S', ('X1','VP')),
        ('X1', ('AUX','NP')),
        ('S', ('book')),
        ('S', ('include')),
        ('S', ('prefer')),
        ('S', ('Verb','NP')),
        ('S', ('X2','PP')),
        ('S', ('Verb','PP')),
        ('NP', 'I'),
        ('NP', 'she'),
        ('NP', 'me'),
        ('NP', 'TWA'),
        ('NP', 'Houston'),
        ('NP', ('Det','Nominal')),
        ('Nominal', 'book'),
        ('Nominal', 'flight'),
        ('Nominal', 'meal'),
        ('Nominal', 'money'),
        ('Nominal', 'Noun'),
        ('Nominal', ('Nominal','PP')),
        ('VP', 'book'),
        ('VP', 'include'),
        ('VP', 'prefer'),
        ('VP', ('Verb','NP')),
        ('VP', ('X2','PP')),
        ('X2', ('Verb','NP')),
        ('VP', ('Verb','PP')),
        ('VP', ('VP','PP')),
        ('PP', ('Preposition','NP')),
        ('Det','the'),
        ('Noun', 'book'),
        ('Noun', 'flight'),
        ('Verb', 'book'),
        ('Preposition', 'through'),
    )
    G = build(CNF)
    T = cky(G, ('book', 'the', 'flight', 'through', 'Houston'))
