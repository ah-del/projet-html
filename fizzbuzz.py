def fizzbuzz():
    nombre = int (input("entrez votre nombre :"))
    
    
    resut = ""
    if nombre%2 == 0 and nombre%3 == 0 : 
        print("fizzbuzz") 
    
    else : 


        if nombre%2 == 0:
            print("fizz")

        else :
            print("le nombre n'est pas divisible par 2")

        if nombre%3 == 0:
            print("buzz")

        else :
            print ("le nombre n'est pas divisible par 3")

    
        
    



    



fizzbuzz()