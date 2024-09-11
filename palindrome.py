def palindrome(mot1):
    mot2 = ""

    taille_bon_mot = len(mot1) -1 #pour la boucle

    while taille_bon_mot >= 0:
        mot2 = mot2 + mot1[taille_bon_mot]
        taille_bon_mot -= 1

    if (mot1 == mot2):
        print(mot1, " est un palindrome")
    else:
        print(mot1," n'est pas un palindrome")

def main():

    mot = input("Entrez un mot :  ")
    palindrome(mot)    

main()