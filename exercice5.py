from math import sqrt

def NombrePremier(nombre):

    pasPremier = 0
    for i in range (2, (int)(sqrt(nombre))):
        divise = nombre%i 

        if(divise == 0):
            pasPremier = pasPremier + 1

    return(pasPremier)


def main():

    nombre = int(input("select un nombre : "))
    pasPremier = NombrePremier(nombre)

    if(pasPremier > 0):
        print("Votre nombre n'est pas premier")
    else:
        print("votre nombre est premier")

main()