import argparse
import os
from fragilite import *
from ameliorations import *
from graphe import *

def metro(graphe, args):
    if args.metro == []:
        files = os.listdir('./')
        for f in files:
            if f.find('METRO') != -1:
                charger_donnees(graphe, f)
    else:
        for m in args.metro:
            fichier = 'METRO_' + m + '.txt'
            charger_donnees(graphe, fichier)

    return graphe

def rer(graphe, args):
    if args.rer == []:
        files = os.listdir('./')
        for f in files:
            if f.find('RER') != -1:
                charger_donnees(graphe, f)
    else:
        for r in args.rer:
            fichier = 'RER_' + r + '.txt'
            charger_donnees(graphe, fichier)
    return graphe

def liste_stations(graphe):
    taille = len(graphe.sommets())
    print(f'le réseau contient les {taille} stations suivantes:\n')
    for nom, station in sorted(graphe.nom_sommets()):
        print(f'{nom} ({station})')
    print()

def articulations(graphe):
    points = points_articulation(graphe)
    nom_stations = [graphe.nom_sommet(u) for u in points]
    taille = len(nom_stations)
    indice = 1
    print(f'Le réseau contient les {taille} points d\'articulation suivants')
    for station in sorted(nom_stations):
        print(f'{indice} : {station}')
        indice += 1
    print()

def afficher_ponts(graphe):
    p = ponts(graphe)
    nom_stations = [(graphe.nom_sommet(u), graphe.nom_sommet(v)) for u, v in p]
    taille = len(nom_stations)
    print(f'Le réseau contient les {taille} ponts suivants')
    for s1, s2 in sorted(nom_stations):
        print(f'- {s1} -- {s2}')
    print()

parser = argparse.ArgumentParser()
parser.add_argument('--metro', nargs='*', default=None)
parser.add_argument('--rer', nargs='*', default=None)
parser.add_argument('--liste-stations', action='store_true')
parser.add_argument('--articulations', action='store_true')
parser.add_argument('--ponts', action='store_true')
parser.add_argument('--ameliorer-articulations', action='store_true')
parser.add_argument('--ameliorer-ponts', action='store_true')

args = parser.parse_args('--metro 7b --liste-stations --ponts --articulations'.split())

G = Graphe()
if args.metro != None:
    print(f'Chargement des lignes {args.metro} de metro ...', end=' ')
    metro(G, args)
    print('terminé')
if args.rer != None:
    print(f'Chargement des lignes {args.rer} de rer ...', end=' ')
    rer(G, args)
    print('terminé')
nombre_sommets = len(G.sommets())
nombre_aretes = len(G.aretes())
print(f'Le réseau contient {nombre_sommets} et {nombre_aretes} arêtes.\n')
if args.liste_stations:
    liste_stations(G)
if args.articulations:
    articulations(G)
if args.ponts:
    afficher_ponts(G)
if args.ameliorer_articulations:
    pass
if args.ameliorer_ponts:
    pass

