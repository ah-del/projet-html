def insertion_de_numero(arr, num):
    i = 0
    while i < len(arr) and arr[i] < num:
        i += 1
    arr.insert(i, num)

# exemple d'utilisation
arr = [1, 3, 4, 7, 8, 10]
print("Tableau avant insertion:", arr)
insertion_de_numero(arr, 45)
print("Tableau après insertion:", arr)
