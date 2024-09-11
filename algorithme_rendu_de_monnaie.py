def rendu_de_monnaie(montant,argent_donner):

    billet = [500, 200, 100, 50, 20, 10, 5]
    piece = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

    a_payer = argent_donner - montant
    a_payer = round(a_payer, 2)

    print(a_payer)

    for i in billet : 
        multiple = 0 

        while(a_payer >= i):
            a_payer = a_payer - i
            a_payer = round(a_payer, 2)
            multiple = multiple + 1 

        if(multiple!= 0):
            print(multiple, "fois le billet : ",i)

    for i in piece:
        multiple = 0 

        while(a_payer >= i):
            a_payer = a_payer - i 
            a_payer = round(a_payer, 2)
            multiple = multiple + 1

        if(multiple!=0):
            print(multiple, "fois la piece : ", i)

    return

def main():

    print("Choisir le montant à payer")
    montant = float(input())
    print("Combien mettez vous d'argent : ")
    argent_donner = float(input())
    rendu_de_monnaie(montant, argent_donner)

main()
