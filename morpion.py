morpion =[
    ["X", "-", "-"],
    ["X", "-", "-"],
    ["Y", "-", "-"]
]

x = "A3"

print(morpion[2][0])


#remplacer A3 par un x

for i in morpion:
    for j in i:
        if (j == "X"):
            print(j)
    print(i)