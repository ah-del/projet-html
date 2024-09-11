def main(): 
    nombre_a_deviner = 10
    print ("entrez votre nombre :")
    nombre_choisi = int(input())

    print(type(nombre_choisi))
    while nombre_choisi != nombre_a_deviner:
        if (nombre_choisi < nombre_a_deviner):
            print("le nombre est plus grand")

        elif nombre_choisi > nombre_a_deviner:
            print("le nombre est plus petit")

        nombre_choisi = int(input())

    print("bravo tu as gagné")
        

        

    
main()