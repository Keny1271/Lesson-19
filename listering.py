L = [4, 5, 1, 2, 0, 9, 3, 6, 7, 8]
print("Original List: ", L)
count = 0
for i in L:
    count += i
avg = count / len(L)
print("sum =" , count)
print("Average = ", avg)
L.sort()
print("Smallest element in the list: ", L[0])
print("Largest element in the list: ", L[-1])