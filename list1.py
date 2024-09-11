from unittest import result


list = [[1,2,3], [4,5,6], [7,8,9]]

result = []

for i in list:
    for y in i:
        print(y)
        if (y %2 == 0):
            result.append("paire")
        else:
            result.append("impair")

print(result)

