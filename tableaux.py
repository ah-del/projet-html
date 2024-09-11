

langages = ["python", "javascript", "html", "mysql"]
chiffres = [[1, 2, 3], [4, 5, 6]]

print(langages[0])
print(chiffres[0])
print(chiffres[0][0])

characters = [-5,0,1,2,3,4,150]
print(characters)

characters.pop()
print(characters)
del characters[0]
print(characters)

var1 = characters[0]
print(var1)

var2 = characters[-1]
print(var2)

characters[0] = var2
characters[-1] = var1

print(characters)

dev = ["php", "python", "javascript", "go"]
print(dev)

var3 = dev[0]
var4 = dev[-1]
dev[0] = var4
dev[-1] = var3
print(dev)