def verifie_mot_de_passe(mdp):

    nb_chiffres = sum(c.isdigit() for c in mdp)
    nb_caracteres_speciaux = sum(c in "&*+/=" for c in mdp)
    nb_lettres = sum(c.isalpha() for c in mdp)
    
    if nb_chiffres >= 3 and nb_caracteres_speciaux >= 3:
        return True
    elif nb_lettres >= 5:
        return True
    elif nb_chiffres < 3 and nb_lettres >= 5 and nb_caracteres_speciaux >= 1:
        return True
    else:
        return False

mdp_utilisateur = input("Entrez votre mot de passe : ")

if verifie_mot_de_passe(mdp_utilisateur):
    print("Le mot de passe est valide")
else:
    print("Le mot de passe est invalide")


