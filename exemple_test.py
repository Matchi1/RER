from graphe import *


G = Graphe()
G.ajouter_sommets(zip('abcdefghijkl', [None] * 12))
G.ajouter_aretes(
    [('a', 'b', None), ('b', 'c', None), ('c', 'a', None), ('c', 'd', None), ('d', 'e', None),
    ('e', 'f', None), ('f', 'd', None), ('a', 'g', None), ('g', 'h', None), ('h', 'a', None),
    ('h', 'i', None), ('i', 'j', None), ('j', 'h', None), ('j', 'k', None), ('k', 'i', None),
    ('i', 'l', None), ('k', 'h', None)])

f = open("test1.dot", "w")
f.write(export_dot(G))
f.close()

G = Graphe()
G.ajouter_sommets(zip('abcdefg', [None] * 7))
G.ajouter_aretes(
    [('a', 'b', None), ('b', 'c', None), ('b', 'd', None), ('c', 'd', None), ('d', 'e', None),
    ('d', 'f', None), ('d', 'g', None), ('e', 'f', None), ('f', 'g', None)])

f = open("test2.dot", "w")
f.write(export_dot(G))
f.close()

G = Graphe()
G.ajouter_sommets(zip('abcdefghijklmn', [None] * 14))
G.ajouter_aretes(
    [('a', 'b', None), ('b', 'c', None), ('c', 'd', None), ('d', 'a', None), ('c', 'e', None),
    ('e', 'f', None), ('f', 'g', None), ('g', 'h', None), ('g', 'i', None), ('g', 'm', None),
    ('i', 'j', None), ('i', 'k', None), ('k', 'l', None), ('l', 'm', None), ('m', 'n', None),
    ('n', 'l', None)])

f = open("test3.dot", "w")
f.write(export_dot(G))
f.close()
