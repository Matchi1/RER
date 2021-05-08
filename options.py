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
        print(f'\t{nom} ({station})')
    print()

def articulations(graphe):
    points = points_articulation(graphe)
    nom_stations = [graphe.nom_sommet(u) for u in points]
    taille = len(nom_stations)
    indice = 1
    print(f'Le réseau contient les {taille} points d\'articulation suivants')
    for station in sorted(nom_stations):
        print(f'\t{indice} : {station}')
        indice += 1
    print()

def afficher_ponts(graphe):
    p = ponts(graphe)
    nom_stations = [(graphe.nom_sommet(u), graphe.nom_sommet(v)) for u, v in p]
    taille = len(nom_stations)
    print(f'Le réseau contient les {taille} ponts suivants')
    for s1, s2 in sorted(nom_stations):
        print(f'\t- {s1} -- {s2}')
    print()

def afficher_amelioration_points_articulation(graphe):
    aretes = amelioration_points_articulation(graphe)
    nom_stations = [(graphe.nom_sommet(u), graphe.nom_sommet(v)) for u, v in aretes]
    print(f'On peut éliminer tous les points d\'articulation du réseau en rajoutant les {len(aretes)} arêtes suivantes:')
    for u, v in sorted(nom_stations):
        print(f'\t- {u} -- {v}')
    print()

def afficher_amelioration_ponts(graphe):
    aretes = amelioration_ponts(graphe)
    nom_stations = [(graphe.nom_sommet(u), graphe.nom_sommet(v)) for u, v in aretes]
    print(f'On peut éliminer tous les ponts du réseau en rajoutant les {len(aretes)} arêtes suivantes:')
    for u, v in sorted(nom_stations):
        print(f'\t- {u} -- {v}')
    print()

def create_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--metro', nargs='*', default=None)
    parser.add_argument('--rer', nargs='*', default=None)
    parser.add_argument('--liste-stations', action='store_true')
    parser.add_argument('--articulations', action='store_true')
    parser.add_argument('--ponts', action='store_true')
    parser.add_argument('--ameliorer-articulations', action='store_true')
    parser.add_argument('--ameliorer-ponts', action='store_true')
    return parser

def chargement_metro(graphe):
    if args.metro == []:
        print(f'Chargement de toutes les lignes de metro ...', end=' ')
    else:
        print(f'Chargement des lignes {args.metro} de metro ...', end=' ')
    metro(graphe, args)
    print('terminé')

def chargement_rer(graphe):
    if args.rer == []:
        print(f'Chargement de toutes les lignes de rer ...', end=' ')
    else:
        print(f'Chargement des lignes {args.rer} de rer ...', end=' ')
    rer(graphe, args)
    print('terminé')

def options(parser):
    G = Graphe()
    if args.metro != None:
        chargement_metro(G)
    if args.rer != None:
        chargement_rer(G)
    print(f'Le réseau contient {len(G.sommets())} sommets et {len(G.aretes())} arêtes.\n')
    d, p, a = numerotations(G)
    print(d)
    print(p)
    print(a)
    print(len(ponts(G)))
    if args.liste_stations:
        liste_stations(G)
    if args.articulations:
        articulations(G)
    if args.ponts:
        afficher_ponts(G)
    if args.ameliorer_articulations:
        afficher_amelioration_points_articulation(G)
    if args.ameliorer_ponts:
        afficher_amelioration_ponts(G)
parser = create_argparser()
args = parser.parse_args()

def main():
    parser = create_argparser()
    args = parser.parse_args()
    options(args)

if __name__ == "__main__":
    main()

