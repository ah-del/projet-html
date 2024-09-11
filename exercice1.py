def TakePositionWithNumber(number):
    listeAlphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numberChose = number
    count = 0
    y = 0
    while(count<=numberChose):
        
        for i in range(0,len(listeAlphabet)):
            if(i == 25):
                y +=1
        i += 1
        count = count + i

    count = count - numberChose
    print("Pour la valeur de : " + str(number) + " la lettre trouvée est le : " + str(listeAlphabet[count]))
    print("il y a : " + str(y) + " alphabet \n")


def main():
    TakePositionWithNumber(10000)
    TakePositionWithNumber(100000)


main()