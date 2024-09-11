import random 

def main():
    value = random.randint(0, 100)
    calcul = value + (value+1) + (value+2)
    div3 = calcul%3
    print(calcul)
    print(div3)

    if(div3 == 0):
        print("le résultat de : " + str(calcul) + " est un multiple de 3 car la division vaut : " + str(div3))
    else:
        print("le résultat n'est pas un mutiple de 3")            

main()