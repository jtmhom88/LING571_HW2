#!/usr/bin/python

import ast

linestring = open('grammar.cnf', 'r').read()

#print linestring


CNF = ast.literal_eval(linestring)

print CNF
