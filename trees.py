#/usr/bin/python

import collections
import ast
import nltk
from nltk.tree import *
from nltk.draw import tree
 


def addleaves(Tree, ltree, rtree ):
    Tree.append(ltree)
    Tree.append(rtree)
    return Tree
    pass

def filter(tree):
    child_nodes = [child.node for child in tree
                   if isinstance(child, nltk.Tree)]
    print child_nodes
    print tree.node
    return  (tree.node == 'S') and ('VP' in child_nodes)

 
if __name__ == '__main__':
    bb = Tree('S', [Tree('VP', ['book']), Tree ('NP', [ Tree ('Det', ['the']), Tree ('Noun', ['Flight'])] ) ] )
    print bb
    print filter(bb)
"""
    root = Tree('S', [])
    print root
    l = Tree('VP', ['book'])
    r = Tree('NP', ['Flight'])
    root = addleaves(root, l, r)
    print root
    ll = Tree('A', ['a'])
    #rr = Tree('B', ['b'])
    newroot = Tree('S', [])
    newroot = addleaves(newroot, ll, root)
    print newroot
    """