from random import *

i = [5 for i in range(4)]
j = [i for i in range(1,7)]
k = [i for i in range(2,13,2)]
l = [[0 for i in range(3)], [1 for i in range(3)], [2 for i in range(3)]]
m = [[j for i in range(3)] for j in range(3)]
n = [i * 3 - 6 for i in range(4)]
o = [[i+j for j in range(3)] for i in range(1,10,3)]


def generer_tab_croissant(n):
    assert n > 0, "n n'est pas positif"
    
    tab = [i for i in range(n)]
    return tab

def generer_tab_decroissant(n):
    assert n > 0, "n n'est pas positif"
    
    tab = [i for i in range(n-1, -1, -1)]
    return tab
    
def generer_tab_melange(n):
    assert n > 0, "n n'est pas positif"
    
    i =  [randint(0,100) for i in range(n)]
    return i
        

