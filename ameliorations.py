from graphe import *
from fragilite import *

def charger_donnees(graphe, fichier):
    charger_sommets = True
    ligne = fichier.split('.')[0]
    with open(fichier, 'r') as f:
        content = f.readlines()

    for line in content:
        if line.find("connexions") != -1:
            charger_sommets = False
        elif line.find("stations") != -1:
            charger_sommets = True
        else:
            if charger_sommets:
                info = line.split(":")
                id, nom = int(info[0]), info[1].rstrip()
                graphe.ajouter_sommet((id, nom))
            else:
                info = line.split("/")
                s1, s2, poids = int(info[0]), int(info[1]), int(info[2].rstrip())
                graphe.ajouter_arete(s1, s2, poids)
                graphe.ajouter_ligne(s1, s2, ligne)
                
def csp(graphe, ponts):
    csp_dict = dict()
    feuilles = dict()
    visite = {s : False for s in sorted(graphe.sommets())}
    indice = 0
    def aux(graphe, s, s_evite, ponts):
        nonlocal indice, est_feuille
        csp_dict[indice].add(s)
        visite[s] = True
        for u, v in ponts:
            if s == u or s == v:
                feuilles[indice] = False
                return
        for v in sorted(graphe.voisins(s)):
            if v != s_evite and not visite[v]:
                aux(graphe, v, s_evite, ponts)
        return

    for u, v in ponts:
        est_feuille = True
        autres_ponts = list(ponts)
        autres_ponts.remove((u, v))
        if not visite[u]:
            csp_dict[indice] = set()
            feuilles[indice] = True
            aux(graphe, u, v, autres_ponts)
            csp_dict[indice] = sorted(csp_dict[indice])
            indice += 1
        if not visite[v]:
            csp_dict[indice] = set()
            feuilles[indice] = True
            aux(graphe, v, u, autres_ponts)
            csp_dict[indice] = sorted(csp_dict[indice])
            indice += 1
    return csp_dict, feuilles

def suppression_csp(graphe, ponts, csp_liste, feuilles):
    chemin = list()
    aretes = list()
    voisins = None
    for i in feuilles:
        chemin.append(csp_liste[i][0])
            
    for i in range(len(chemin) - 1):
        if (chemin[i], chemin[i + 1]) not in ponts:
            aretes.append((chemin[i], chemin[i + 1]))
        else:
            voisins = graphe.voisins(chemin[i])
            if len(voisins) > 1:
                for v in voisins:
                    if v != chemin[i + 1]:
                        chemin[i] = v
                        break
            else:
                voisins = graphe.voisins(chemin[i + 1])
                for v in voisins:
                    if v != chemin[i]:
                        chemin[i + 1] = v
                        break
            aretes.append((chemin[i], chemin[i + 1]))
    return aretes

def amelioration_ponts(graphe):
    p = ponts(graphe)
    csp_liste, feuilles = csp(graphe, p)
    aretes = suppression_csp(graphe, p, csp_liste, feuilles)
    return aretes

def plus_vieux(debut, articulations):
    sommet = None
    for elt in articulations:
        if sommet == None:
            sommet = elt
        elif debut[sommet] < debut[elt]:
            sommet = elt
    return sommet

def suppression_points_articulation_racine(graphe, racines, parent):
    aretes = list()
    chemin = list()
    for r in racines:
        for v in graphe.voisins(r):
            if parent[v] == r:
                chemin.append(v)
    chemin = sorted(chemin)
    for i in range(len(chemin) - 1):
        aretes.append((chemin[i], chemin[i + 1])) 
    return aretes

def ancetre_point_articulation(depart, parents, articulations):
    if depart in articulations:
        return depart
    elif depart == None:
        return None
    return ancetre_point_articulation(parents[depart], parents, articulations)

def descendant(graphe, s, debut, ancetre):
    for v in sorted(graphe.voisins(s)):
        if ancetre[v] >= debut[s]:
            return v
    return None

def racine(s, parents):
    if parents[s] == None:
        return s
    return racine(parents[s], parents)

def amelioration_points_articulation(graphe):
    debut, parents, ancetre = numerotations(graphe)
    articulations = points_articulation(graphe) 
    temp = articulations.copy()
    racines = set()
    aretes = list()
    desc = None

    for _ in range(len(articulations)):
        sommet = plus_vieux(debut, temp)
        desc = descendant(graphe, sommet, debut, ancetre)
        if desc == None:
            temp.remove(sommet)
        elif parents[sommet] != None:
            r = racine(sommet, parents)
            racines.add(r)
            aretes.append((r, desc))
            ancetre[sommet] = debut[r]
            temp.remove(sommet)
    aretes.extend(suppression_points_articulation_racine(graphe, racines, parents))
    return aretes
