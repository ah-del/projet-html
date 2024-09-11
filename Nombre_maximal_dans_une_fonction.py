def NomFct (liste):

	size = len(liste)
	y = liste[0]
    
	for i in range(1, size):
		if y>liste[i]:
			print(y)
		
		else : 
			y = liste[i]
	
	return(y)