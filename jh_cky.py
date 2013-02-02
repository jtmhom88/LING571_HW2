#/usr/bin/python

import collections
import ast
import nltk
from nltk.tree import *
from nltk.draw import tree
 
class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def printpair(self):
        print self.x
        print self.y

def build(CNF):
    G = collections.defaultdict(list)
    for left, right in CNF:
        G[right].append(left)
    #print G
    return G

def addleaves(Tree, ltree, rtree ):
    Tree.append(ltree)
    Tree.append(rtree)
    return Tree
    pass
 
def cky(G, W):
    # cell of table is a list of pairs (tag, tree)
    blankpair = Pair('', Tree('',[]))
    Table = [[ [blankpair] for j in range(len(W)+1)] for i in range(len(W))]
    for j in range(1, len(W)+1):
        theword = W[j-1]
        taglist = G.get(theword, [])
        # iterate the tags, and make a pair entry for each
        for tag in taglist:
            tagtree = Tree(tag, [theword])
            thispair = Pair(tag, tagtree)
            #thispair.printpair()
            nowcell = Table[j-1][j]
            #print nowcell
            Table[j-1][j].append(thispair)
        for e in Table[j-1][j]:
            #print "[%d,%d]: %r %r" % (j-1, j, e.x, e.y)
            pass

        for i in range(j-2, -1, -1):
            for k in range(i+1, j):
                for e in Table[i][k]:
                    for f in Table[k][j]:
                        #e.printpair()
                        #f.printpair()
                        # each elem of Table is a pair
                        taglist = G.get((e.x,f.x), [])
                        #print "taglist e.x f.x %r %r %r" % (taglist,e.x,f.x)
                        for tag in taglist:
                            tagtree = Tree(tag, [])
                            tagtree.append(e.y)
                            tagtree.append(f.y)
                            #print "tagtree %r" % (tagtree)
                            thispair = Pair(tag, tagtree)
                            #thispair.printpair()
                            nowcell = Table[i][j]
                            #print "nowcell %r" % nowcell
                            Table[i][j].append(thispair)
                        for ee in Table[i][j]:
                            #print "[%d,%d]: %r %r" % (i, j, ee.x, ee.y)
                            pass
    # Final Answer is in upper right cell 
    # cell is list of pairs
    outstring = ''
    finalcell = Table[0][len(W)]
    #print "\nFINAL PARSE TREES:"
    n = 0
    for e in finalcell:
        # each element e is a pair
        finaltag = e.x
        finaltree = Tree('TOP', [e.y])
        if (e.x == 'S' or e.x == 'SQ' or e.x == 'FRAG'):
            #print "FINAL tag: %s" % finaltag
            #print "FINAL tree %d:\n%s" % (n,finaltree)
            #print "\n"
            outstring += "\nFINAL tree %d:\n%s\n" % (n,finaltree)
            n += 1

    return (outstring)
 
 
if __name__ == '__main__':
    outfile = open('hw2.out','w')
    grammarfile = 'grammar.cnf'
    #grammarfile = 'julie.cnf'
    linestring = open(grammarfile, 'r').read()
    CNF = ast.literal_eval(linestring)

    G = build(CNF)
    #T = cky(G, ('book', 'the', 'flight', 'through', 'Houston'))
    #T = cky(G, ('work', 'accelerates', 'the', 'growth', 'of', 'muscles'))
    #T = cky(G, ('muscles', 'grow', 'in', 'response', 'to', 'work'))

    # Iterate through all the files in inputfile.txt
    i = 0
    temp = tok = ll = []
    infile = open('inputfile.txt','r')
    for line in infile:
        temp = line.strip()
        ll.append(temp)
        tok = nltk.word_tokenize(temp)
        T = cky(G,tok)
        outfile.write("-----------------------------\n")
        outfile.write("Line %d: %s" % (i,line))
        outfile.write(T)
        #print "-----------------------------"
        #print "Line %d: %s" % (i,line)
        #print T
        #print "\n"
        #if i> 4:
        #    break
        i += 1
        pass


