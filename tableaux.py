from random import *

i = [5 for i in range(4)]
j = [i for i in range(1,7)]
k = [i for i in range(2,13,2)]
l = [[0 for i in range(3)], [1 for i in range(3)], [2 for i in range(3)]]
m = [[j for i in range(3)] for j in range(3)]
n = [i * 3 - 6 for i in range(4)]

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
o = [[i+j for j in range(3)] for i in range(1,10,3)]


def generer_tab_croissant(n):
    if n > 0:
        tab = [i for i in range(n)]
    return tab

def generer_tab_decroissant(n):
    if n > 0:
        tab = [i for i in range(n-1, -1, -1)]
        return tab
    
def generer_tab_melange(n):
    if n > 0:
        i =  [randint(0,100) for i in range(n)]
        return i
        
