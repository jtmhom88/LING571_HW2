#/usr/bin/python

import collections
import ast
from nltk.tree import *
from nltk.draw import tree
 
def build(CNF):
    G = collections.defaultdict(list)
    for left, right in CNF:
        G[right].append(left)
    print G
    return G
 
def cky(G, W):
    Table = [[[] for j in range(len(W)+1)] for i in range(len(W))]
    Trees = [[[] for j in range(len(W)+1)] for i in range(len(W))]
    for j in range(1, len(W)+1):
        theword = W[j-1]
        taglist = G.get(theword, [])
        Table[j-1][j] += taglist
        for tag in taglist:
            tagtree = Tree(tag, [theword])
            Trees[j-1][j].append(tagtree)
            print "Tree %r" % (tagtree)
            print "Treej-1,j [%d,%d]: %r" % (j-1,j,Trees[j-1][j])
        #print "j-1,j[%d,%d]: %s %r" % (j-1, j, W[j-1], G.get(W[j-1]))
        print "Tj-1,j [%d,%d]=%r" % (j-1,j,Table[j-1][j])
        for i in range(j-2, -1, -1):
            #print "i %d" % i
            for k in range(i+1, j):
                print "k %d i %d j %d " % (k,i,j)
                for x in Table[i][k]:
                    #print "Ti,k [%d,%d]=%r" % (i,k,Table[i][k])
                    for y in Table[k][j]:
                        #print "Tk,j [%d,%d]=%r" % (k,j,Table[k][j])
                        Table[i][j] += G.get((x,y), [])
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
                        print "Ti,j[%d,%d]: %r " % (i,j,Table[i][j])
    print "FINAL Table[0][%d]=%r" % (len(W),Table[0][len(W)])
    return Table
 
if __name__ == '__main__':
    #grammarfile = 'grammar.cfg'
    grammarfile = 'julie.cnf'
    linestring = open(grammarfile, 'r').read()
    CNF = ast.literal_eval(linestring)

    G = build(CNF)
    T = cky(G, ('book', 'the', 'flight', 'through', 'Houston'))
    #T = cky(G, ('work', 'accelerates', 'the', 'growth', 'of', 'muscles'))


