#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy

'''

Desafio clavis
03012017

'''
'''
class Maze(object):
    def __init__(self, size=0, M=[]):
        self.Y=size[0]
        self.X=size[1]
        self.M=M
    def __repr__(self):
        s=""
        for y in range(len(M)):
            for x in range(len(M[y])):
                s+="{:>2}".format(M[y][x])
            s+="\n"
    def pos(x, y):
        self.x=x
        self.y=y
'''

def print_maze(M):
    s=""
    for y in range(len(M)):
        for x in range(len(M[y])):
            s+="{:>2}".format(M[y][x])
        s+="\n"
    print s


def parse(args):
    Y=int(args[1])
    X=int(args[2])
    L=map(int, args[3].split(","))
    start=map(int, args[4].split(","))
    M=[]
    for y in xrange(Y):
        line=[]
        for x in xrange(X):
            line+=[L.pop(0)]
        M+=[line]
    # numbers start from 0 internally
    return [Y-1, X-1], M, [start[0], start[1]]


def solve(size, M, step):
    Y=size[0]
    X=size[1]
    y=step[0]
    x=step[1]

    if M[y][x]==0: # its OK to step here
        print_maze(M)
        print
        M[y][x]=1 # mark my position in map
        if (x==0 or x==X or y==0 or y==Y): # I am at an exit!
            return M
        else:
            # Try walking around, first let's step up
            solution=solve(size, deepcopy(M), [y-1, x])
            if solution:
                return solution
            # step down
            solution=solve(size, deepcopy(M), [y+1, x])
            if solution:
                return solution
            # step left
            solution=solve(size, deepcopy(M), [y, x-1])
            if solution:
                return solution
            # step right
            solution=solve(size, deepcopy(M), [y, x+1])
            if solution:
                return solution
            else:
                return 0
    else:  # stepping into an invalid position returns no solution
        return 0


if __name__ == '__main__':
    try:
        size, M, start=parse(sys.argv)
    except Exception, e:
        sys.exit("""
         Erro: [{}] processando parametros.
         Este deve ser o formato para rodar este programa:
        ./programa 3 3 -1,0,-1,0,0,-1,-1,-1,-1 1,1
        """.format(e))

    # maze=Maze(size, M)
    M=solve(size, M, start)
    print_maze(M)
