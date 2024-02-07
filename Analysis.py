def analyser_mot_de_passe(mot_de_passe):
    erreurs = []  # Liste pour stocker les messages d'erreur

    # Vérifications
    if len(mot_de_passe) < 10: # Si le longueur du mot de passe est strictement inférieur à 10, on l'ajoute à la liste des erreurs
        erreurs.append(" au moins 10 caractères") 

    if not any(char.islower() for char in mot_de_passe): # Si le mot de passe ne possède pas au moins un caractère en minuscule, on l'ajoute à la liste des erreurs
        erreurs.append("au moins un caractère en minuscule")

    if not any(char.isupper() for char in mot_de_passe): # Si le mot de passe ne possède pas au moins un caractère en majuscule, on l'ajoute à la liste des erreurs
        erreurs.append("au moins un caractère en majuscule")

    if not any(char.isdigit() for char in mot_de_passe): # Si le mot de passe ne possède pas au moins un chiffre, on l'ajoute à la liste des erreurs
        erreurs.append("au moins un chiffre")
    

    # Affichage des Résultats
    if not erreurs and 11 <= len(mot_de_passe) <= 15 :  # Si la liste des erreurs est toujours vide, et que le mot de passe passe est entre 11 compris et 15 compris, le mot de passe est moyen
        print("Votre mot de passe est moyen.")
    elif not erreurs and 15 < len(mot_de_passe) <= 18 :  # Si la liste des erreurs est toujours vide, et que le mot de passe passe est entre 15 exclu et 18 compris, le mot de passe est fort
        print("Votre mot de passe est fort.")
    elif not erreurs and len(mot_de_passe) > 18 :  # Si la liste des erreurs est toujours vide, et que le mot de passe passe est strictement supérieur à 18, le mot de passe est très fort
        print("Votre mot de passe est très fort.")
    else:
        print("Votre mot de passe doit contenir" + ", \n".join(erreurs)) # Si la liste des erreurs n'est pas vide, on lui ajoute toutes les erreurs que l'utilisateur a commis et on imprime


    ### ESTIMATION DU TEMPS DE CRACKAGE ###

    taille_password = len(mot_de_passe) #taille du mot de passe

    estimation_essaie = 10**9 #Exemple raisonnable de tentative d'essaie par seconde (environ 1 000 000 de tests par secondes)
        
    nombre_de_caractere_possible = 94 #Nombre de caractères possibles (10 Chiffres + 26 Lettres Majuscule + 26 Lettres Minuscule + 32 Symboles)

    nombre_de_combinaison = nombre_de_caractere_possible ** taille_password # Le nombre de combinaison se traduit par toutes les possibilités qu'un attanquant pourrait effectuer par force brute

    temps_crackage_secondes = nombre_de_combinaison / estimation_essaie # Temps en seconde(s) qu'il faut à l'attaquant pour craquer le mot de passe avec une fréquence d'1 milliard de tests par secondes

    temps_crackage_jours = temps_crackage_secondes / 3600 / 24 # Temps en jours qu'il faut à l'attaquant pour craquer le mot de passe avec une fréquence d'1 milliard de tests par secondes

    temps_crackage_années = temps_crackage_secondes / 3600 / 24 / 30 / 365.25 # Temps en année(s) qu'il faut à l'attaquant pour craquer le mot de passe avec une fréquence d'1 milliard de tests par secondes


    print(f"Le temps de crackage est estimé à environ {temps_crackage_secondes} seconde(s), équivalent à environ {temps_crackage_jours} jours, c'est-à-dire {temps_crackage_années} année(s)")



# Demander à l'utilisateur d'entrer un mot de passe
mot_de_passe = input("Entrez un mot de passe : ")
analyser_mot_de_passe(mot_de_passe)





