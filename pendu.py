def main(): 
    mot_a_decouvrir = "bonjour"
    print ("ajouter une lettre :")
    lettre_choisie = (input())
    

    print(type(lettre_choisie))

    while True:
        compteur = 1

        if (lettre_choisie in mot_a_decouvrir ):
            print ("la lettre est dans le mot")
            for i in mot_a_decouvrir:
                if i == lettre_choisie:
                    print(compteur)
                compteur = compteur +1

        
        else : 
            print ("la lettre n'est pas dans le mot")








        
        

        
            

        lettre_choisie = (input())

    

        
main()