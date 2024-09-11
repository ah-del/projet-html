def main():
    reslut= False
    i = 0
    while(reslut == False ):
        
        N0 = 10*i+7
        N1 = 7*(13+i)+3

        if(10*i+7-(7*(13+i)+3) == 0):
            print(i)
            reslut = True
        
        i+=1

main()