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
                s1, s2 , poids = int(info[0]), int(info[1]), int(info[2].rstrip())
                graphe.ajouter_arete(s1, s2, poids)
                graphe.ajouter_ligne(s1, s2, ligne)
                
