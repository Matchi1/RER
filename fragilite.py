def numerotations(graphe):
    debut = {sommet : 0 for sommet in graphe.sommets()}
    parent = {sommet : None for sommet in graphe.sommets()}
    ancetre = {sommet : 100 for sommet in graphe.sommets()}
    instant = 0
    def numerotation_recursive(s):
        nonlocal instant
        instant += 1
        debut[s] = ancetre[s] = instant
        for t in sorted(graphe.voisins(s)):
            if debut[t] != 0:
                if parent[s] != t:
                    ancetre[s] = min(ancetre[s], debut[t])
            else:
                parent[t] = s
                numerotation_recursive(t)
                ancetre[s] = min(ancetre[s], ancetre[t])
    for v in sorted(graphe.sommets()):
        if debut[v] == 0:
            numerotation_recursive(v)
    return debut, parent, ancetre

def degre_sortant(graphe, debut, parent, ancetre, depart):
    deg_sortant = 0
    for s in sorted(graphe.sommets()):
        if ancetre[s] == debut[depart]:
            if parent[s] == depart:
                deg_sortant += 1
    return deg_sortant

def points_articulation(graphe):
    debut, parent, ancetre = numerotations(graphe)
    articulations = []
    racines = [sommet for sommet in graphe.sommets() if parent[sommet] == None]
    for depart in racines:
        if degre_sortant(graphe, debut, parent, ancetre, depart) >= 2: 
            articulations.append(depart)
    racines.append(None)
    for v in sorted(graphe.sommets()):
        if parent[v] not in racines and ancetre[v] >= debut[parent[v]]:
            if parent[v] not in articulations:
                articulations.append(parent[v])
    return articulations

def ponts(graphe):
    p = list()
    debut, parent, ancetre = numerotations(graphe)
    for v in sorted(graphe.sommets()): 
        if parent[v] != None:
            if ancetre[v] > debut[parent[v]]:
                p.append(tuple(sorted((parent[v], v))))
    return p
