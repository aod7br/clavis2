#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Desafio1 clavis
03012017
'''

from sys import exit, argv
from copy import deepcopy

def entries(size, M):
    '''
    list all available entry points (if any)
    '''
    Y, X=size[0], size[1]
    entry_list=[]
    for y in range(Y):
        if M[y][0]==0:
            entry_list+=[[y, 0]]
        if M[y][X]==0:
            entry_list+=[[y, X]]
    for x in range(X):
        if M[0][x]==0:
            entry_list+=[[0, x]]
        if M[Y][x]==0:
            entry_list+=[[Y, x]]
    return entry_list


def stringfy(M):
    '''
    returns a string representation of maze array
    '''
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
    # positions start from 0 internally
    return [Y-1, X-1], M, [start[0], start[1]]


def solve(size, M, step, count=0):
    '''
    this function will attempt to use recursion to find an exit
    from the maze. What it does is walk to an available direction
    and backtrack if it finds a block
    '''
    Y=size[0]
    X=size[1]
    y=step[0]
    x=step[1]
    print stringfy(M)
    if (0<=x and x<=X and 0<=y and y<=Y) and M[y][x]==0: # its OK to step here
        M[y][x]=1 # mark my position in map
        # I am at an exit, and its not a start, so its a solution!
        if (x==0 or x==X or y==0 or y==Y) and count:
            return M
        else:
            count+=1
            # Try walking around
            solution=solve(size, deepcopy(M), [y-1, x], count) # step up
            if solution:
                return solution
            solution=solve(size, deepcopy(M), [y+1, x], count) # step down
            if solution:
                return solution
            solution=solve(size, deepcopy(M), [y, x-1], count) # step left
            if solution:
                return solution
            # last try
            solution=solve(size, deepcopy(M), [y, x+1], count) # step right
            if solution:
                return solution
            else:
                return 0
    else:  # stepping into an invalid position returns no solution
        return 0

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    try:
        size, M, start=parse(argv)
    except Exception, e:
        exit("""
         Erro: [{}] processando parametros.
         Este deve ser o formato para rodar este programa:

        ./programa Y X lista y,x

        ex: ./programa 3 3 -1,0,-1,0,0,-1,-1,-1,-1 1,1
        """.format(e))

    solution=None
    for start in entries(size, M):
        solution=solve(size, deepcopy(M), start)
        if solution:
            break

    print stringfy(solution) if solution else 0
