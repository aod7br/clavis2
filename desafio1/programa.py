#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy

'''
Desafio clavis
03012017
'''

def stringfy(M):
    s=""
    for y in range(len(M)):
        for x in range(len(M[y])):
            s+="{:>2}".format(M[y][x])
        s+="\n"
    return s


def parse(args):
    '''
    parse cmdline parameters
    '''
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
    if not(0<=start[0] and start[0]<=Y and 0<=start[1] and start[1]<=X):
        raise Exception('inicio deve ser menor que tamanho do labirinto')
    # numbers start from 0 internally
    return [Y-1, X-1], M, [start[0], start[1]]


def solve(size, M, step):
    '''
    this function will attempt to use recursion to find an exit
    from the maze. What it does is walk to an available direction
    and backtrack if it finds a block
    '''
    Y=size[0]
    X=size[1]
    y=step[0]
    x=step[1]
    if M[y][x]==0: # its OK to step here
        M[y][x]=1 # mark my position in map
        if (x==0 or x==X or y==0 or y==Y): # I am at an exit!
            return M
        else:
            # Try walking around
            solution=solve(size, deepcopy(M), [y-1, x]) # step up
            if solution:
                return solution
            solution=solve(size, deepcopy(M), [y+1, x]) # step down
            if solution:
                return solution
            solution=solve(size, deepcopy(M), [y, x-1]) # step left
            if solution:
                return solution
            # last try
            solution=solve(size, deepcopy(M), [y, x+1]) # step right
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
        exit("""
         Erro: [{}] processando parametros.
         Este deve ser o formato para rodar este programa:

        ./programa Y X lista y,x

        ex: ./programa 3 3 -1,0,-1,0,0,-1,-1,-1,-1 1,1
        """.format(e))

    M=solve(size, M, start)
    print stringfy(M) if M else 0
